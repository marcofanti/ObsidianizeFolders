import logging
from dataclasses import dataclass, field
from pathlib import Path

from obsidianize.config import Config
from obsidianize.db import Database, FileRecord
from obsidianize.imports import extract_imports, resolve_wikilinks
from obsidianize.llm import summarize
from obsidianize.notes import archive_note, note_subpath, rename_note, write_index, write_note
from obsidianize.scanner import scan_project

logger = logging.getLogger(__name__)


@dataclass
class SyncResult:
    added: list[str] = field(default_factory=list)
    updated: list[str] = field(default_factory=list)
    moved: list[str] = field(default_factory=list)
    archived: list[str] = field(default_factory=list)
    failed: list[tuple[str, str]] = field(default_factory=list)
    unchanged: int = 0


def sync_project(root_path: Path, db: Database, config: Config) -> SyncResult:
    result = SyncResult()
    root_path = root_path.resolve()

    project = db.get_project(str(root_path))
    if not project:
        raise ValueError(f"Project not registered: {root_path}. Run 'obsidianize add' first.")

    vault_folder = config.vault_path / project.vault_folder
    vault_folder.mkdir(parents=True, exist_ok=True)

    # ── 1. Scan disk ─────────────────────────────────────────────────────────
    scanned = scan_project(root_path, config.include_extensions, config.exclude_dirs)
    scanned_map = {f.relative_path: f for f in scanned}

    # ── 2. Load DB state ─────────────────────────────────────────────────────
    db_files: dict[str, FileRecord] = {
        f.relative_path: f for f in db.get_active_files(project.id)
    }

    # ── 3. Classify changes ──────────────────────────────────────────────────
    new_paths = set(scanned_map) - set(db_files)
    deleted_paths = set(db_files) - set(scanned_map)
    existing_paths = set(scanned_map) & set(db_files)

    # Move detection: deleted hash matches a new file's hash
    new_by_hash = {scanned_map[p].file_hash: scanned_map[p] for p in new_paths}

    moves: dict[str, FileRecord] = {}  # new_path → old FileRecord
    true_deletes: set[str] = set()

    for old_path in deleted_paths:
        old_record = db_files[old_path]
        if old_record.file_hash in new_by_hash:
            new_file = new_by_hash[old_record.file_hash]
            moves[new_file.relative_path] = old_record
        else:
            true_deletes.add(old_path)

    true_new = new_paths - set(moves.keys())
    modified = {p for p in existing_paths if scanned_map[p].file_hash != db_files[p].file_hash}
    result.unchanged = len(existing_paths) - len(modified)

    # All currently-on-disk paths for wikilink resolution
    tracked_paths = set(scanned_map.keys())

    # ── 4. Handle moves ──────────────────────────────────────────────────────
    for new_path, old_record in moves.items():
        new_file = scanned_map[new_path]
        old_note = vault_folder / old_record.vault_subdir / old_record.note_filename \
            if old_record.vault_subdir else vault_folder / old_record.note_filename
        new_subpath = note_subpath(new_file.vault_subdir, new_file.note_stem)
        new_note = vault_folder / new_subpath

        if old_note.exists():
            rename_note(old_note, new_note)

        db.upsert_file(
            project.id, new_path,
            new_file.file_hash, new_file.note_stem,
            new_file.vault_subdir, "active",
        )
        db.mark_archived(project.id, old_record.relative_path)
        result.moved.append(new_path)
        logger.info("Moved: %s → %s", old_record.relative_path, new_path)

    # ── 5. Handle true deletes (archive) ─────────────────────────────────────
    for old_path in true_deletes:
        old_record = db_files[old_path]
        old_note = vault_folder / old_record.vault_subdir / old_record.note_filename \
            if old_record.vault_subdir else vault_folder / old_record.note_filename
        if old_note.exists():
            archive_note(old_note, vault_folder)
        db.mark_archived(project.id, old_path)
        result.archived.append(old_path)
        logger.info("Archived: %s", old_path)

    # ── 6. Summarize new and modified files ───────────────────────────────────
    to_process = [(p, "added") for p in true_new] + [(p, "updated") for p in modified]

    for rel_path, change_type in to_process:
        scanned_file = scanned_map[rel_path]
        try:
            content = scanned_file.path.read_text(encoding="utf-8", errors="replace")
            summary = summarize(content, rel_path, config)
            raw_imports = extract_imports(scanned_file.path, content)
            wikilinks = resolve_wikilinks(raw_imports, tracked_paths)
            note_path = write_note(
                vault_folder,
                rel_path,
                scanned_file.note_stem,
                scanned_file.vault_subdir,
                summary,
                wikilinks,
            )
            db.upsert_file(
                project.id, rel_path,
                scanned_file.file_hash, scanned_file.note_stem,
                scanned_file.vault_subdir, "active",
            )
            if change_type == "added":
                result.added.append(rel_path)
            else:
                result.updated.append(rel_path)
            logger.info("%s: %s", change_type.capitalize(), rel_path)
        except Exception as exc:
            result.failed.append((rel_path, str(exc)))
            logger.warning("Failed to process %s: %s", rel_path, exc)

    # ── 7. Rebuild indices ───────────────────────────────────────────────────
    active_records = [
        (f.vault_subdir, f.note_filename.removesuffix(".md"))
        for f in db.get_active_files(project.id)
    ]
    write_index(vault_folder, active_records, config.max_index_entries)

    db.update_project_sync_time(project.id)
    return result
