import hashlib
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ScannedFile:
    path: Path
    relative_path: str  # relative to project root
    file_hash: str
    vault_subdir: str   # '' for root files, subdir name for files in subdirectories
    note_stem: str      # filename stem used for note naming (Q2-B: just the stem)


def scan_project(
    root: Path,
    include_extensions: list[str],
    exclude_dirs: list[str],
) -> list[ScannedFile]:
    """
    Walk the project root and return important files up to 3 levels deep.

    Structure:
      root/file            → vault_subdir=''
      root/subdir/file     → vault_subdir='subdir'
      root/subdir/sub/file → vault_subdir='subdir'  (flat inside vault subdir)
    """
    root = root.resolve()
    ext_set = set(include_extensions)
    exclude_set = set(exclude_dirs)
    results: list[ScannedFile] = []

    # Depth 0: root-level files (skip dotfiles)
    for entry in root.iterdir():
        if entry.is_file() and not entry.name.startswith(".") and entry.suffix in ext_set:
            results.append(_make(entry, root, vault_subdir=""))

    # Depth 1: root subdirs → vault subfolders (skip dotfolders and excluded dirs)
    for entry in root.iterdir():
        if not entry.is_dir() or entry.name.startswith(".") or entry.name in exclude_set:
            continue
        subdir_name = entry.name

        # Direct files in subdir (skip dotfiles)
        for child in entry.iterdir():
            if child.is_file() and not child.name.startswith(".") and child.suffix in ext_set:
                results.append(_make(child, root, vault_subdir=subdir_name))

        # Depth 2: one more level within subdir (flat into same vault subdir, no new folder)
        for subentry in entry.iterdir():
            if not subentry.is_dir() or subentry.name.startswith(".") or subentry.name in exclude_set:
                continue
            for child in subentry.iterdir():
                if child.is_file() and not child.name.startswith(".") and child.suffix in ext_set:
                    results.append(_make(child, root, vault_subdir=subdir_name))

    return results


def hash_file(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def _make(path: Path, root: Path, vault_subdir: str) -> ScannedFile:
    return ScannedFile(
        path=path,
        relative_path=str(path.relative_to(root)),
        file_hash=hash_file(path),
        vault_subdir=vault_subdir,
        note_stem=path.stem,
    )
