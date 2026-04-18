import re
from pathlib import Path


def extract_imports(file_path: Path, content: str) -> list[str]:
    """Return raw import strings found in Python, JS, or TS source files."""
    ext = file_path.suffix.lower()
    if ext == ".py":
        return _python_imports(content)
    if ext in {".js", ".ts", ".jsx", ".tsx"}:
        return _js_imports(content)
    return []


def resolve_wikilinks(
    raw_imports: list[str],
    tracked_relative_paths: set[str],
) -> list[str]:
    """
    Convert raw import strings to note stem names for files that are tracked in the DB.
    Skips third-party packages and out-of-scope files.
    """
    wikilinks: list[str] = []
    for imp in raw_imports:
        candidates = _import_to_candidates(imp)
        for candidate in candidates:
            if candidate in tracked_relative_paths:
                wikilinks.append(_path_to_note_stem(candidate))
                break
    # deduplicate while preserving order
    seen: set[str] = set()
    return [w for w in wikilinks if not (w in seen or seen.add(w))]  # type: ignore[func-returns-value]


# ── Private helpers ──────────────────────────────────────────────────────────

def _python_imports(content: str) -> list[str]:
    modules: list[str] = []
    for m in re.finditer(r"^from\s+([\w.]+)\s+import", content, re.MULTILINE):
        modules.append(m.group(1))
    for m in re.finditer(r"^import\s+([\w.,\s]+)", content, re.MULTILINE):
        for part in m.group(1).split(","):
            name = part.strip().split(" ")[0].strip()
            if name:
                modules.append(name)
    return modules


def _js_imports(content: str) -> list[str]:
    modules: list[str] = []
    for m in re.finditer(
        r"""(?:import|export).*?from\s+['"]([^'"]+)['"]""", content, re.MULTILINE
    ):
        modules.append(m.group(1))
    for m in re.finditer(r"""require\(\s*['"]([^'"]+)['"]\s*\)""", content):
        modules.append(m.group(1))
    return modules


def _import_to_candidates(imp: str) -> list[str]:
    """Generate possible relative file paths from a raw import string."""
    # Strip leading ./ or ../
    clean = re.sub(r"^\.{1,2}/", "", imp)
    # Convert Python dot notation (src.utils) to path (src/utils)
    base = clean.replace(".", "/")
    return [
        f"{base}.py",
        f"{base}.js",
        f"{base}.ts",
        f"{base}/index.js",
        f"{base}/index.ts",
        f"{base}/__init__.py",
    ]


def _path_to_note_stem(relative_path: str) -> str:
    """Convert 'src/utils.py' to 'src-utils'."""
    p = Path(relative_path)
    return str(p.with_suffix("")).replace("/", "-").replace("\\", "-")
