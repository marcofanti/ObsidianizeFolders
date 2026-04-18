from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


def vault_folder_name(project_root: Path) -> str:
    """'/Users/mfanti/AgenticAI/MyProject' → 'Users-mfanti-AgenticAI-MyProject'"""
    return str(project_root.resolve()).lstrip("/").replace("/", "-")


def note_subpath(vault_subdir: str, note_stem: str) -> str:
    """Return the note path relative to the vault project folder."""
    filename = f"{note_stem}.md"
    return f"{vault_subdir}/{filename}" if vault_subdir else filename


def write_note(
    vault_folder: Path,
    relative_path: str,
    note_stem: str,
    vault_subdir: str,
    summary: str,
    wikilinks: list[str],
) -> Path:
    target_dir = vault_folder / vault_subdir if vault_subdir else vault_folder
    target_dir.mkdir(parents=True, exist_ok=True)
    note_path = target_dir / f"{note_stem}.md"

    language = Path(relative_path).suffix.lstrip(".")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    frontmatter = (
        f"---\n"
        f"file_path: {relative_path}\n"
        f"project: {vault_folder.name}\n"
        f"last_updated: {today}\n"
        f"language: {language}\n"
        f"---\n\n"
    )

    deps_section = ""
    if wikilinks:
        links = "\n".join(f"- [[{link}]]" for link in wikilinks)
        deps_section = f"\n\n## Dependencies\n{links}"

    note_path.write_text(frontmatter + summary + deps_section, encoding="utf-8")
    return note_path


def write_index(
    vault_folder: Path,
    active_records: list[tuple[str, str]],  # list of (vault_subdir, note_stem)
    max_entries: int,
) -> None:
    """
    Write one _index.md per vault subfolder, plus a root _index.md that lists
    everything grouped by subfolder (Q3-B).
    """
    # Group by subdir
    by_subdir: dict[str, list[str]] = defaultdict(list)
    for vault_subdir, note_stem in active_records:
        by_subdir[vault_subdir].append(note_stem)

    # Per-subfolder indices
    for subdir, stems in by_subdir.items():
        if not subdir:
            continue
        subdir_path = vault_folder / subdir
        subdir_path.mkdir(parents=True, exist_ok=True)
        entries = sorted(stems)[:max_entries] if max_entries > 0 else sorted(stems)
        links = "\n".join(f"- [[{stem}]]" for stem in entries)
        (subdir_path / "_index.md").write_text(
            f"# {subdir}\n\n{links}\n", encoding="utf-8"
        )

    # Root index: all notes grouped by subfolder
    root_lines: list[str] = [f"# {vault_folder.name}\n"]

    # Root-level notes first
    root_stems = sorted(by_subdir.get("", []))
    if root_stems:
        entries = root_stems[:max_entries] if max_entries > 0 else root_stems
        root_lines.append("\n".join(f"- [[{s}]]" for s in entries))

    # Then each subdir group
    for subdir in sorted(k for k in by_subdir if k):
        stems = sorted(by_subdir[subdir])
        entries = stems[:max_entries] if max_entries > 0 else stems
        root_lines.append(f"\n## {subdir}")
        root_lines.append("\n".join(f"- [[{subdir}/{s}]]" for s in entries))

    (vault_folder / "_index.md").write_text("\n".join(root_lines) + "\n", encoding="utf-8")


def archive_note(note_path: Path, vault_folder: Path) -> Path:
    """Move a note into Archive/ at the vault project folder root."""
    archive_dir = vault_folder / "Archive"
    archive_dir.mkdir(exist_ok=True)
    dest = archive_dir / note_path.name
    note_path.rename(dest)
    return dest


def rename_note(old_note_path: Path, new_note_path: Path) -> None:
    """Move a note from old_note_path to new_note_path (handles cross-subdir moves)."""
    new_note_path.parent.mkdir(parents=True, exist_ok=True)
    old_note_path.rename(new_note_path)
