# Design Decisions

Decisions recorded here exist to be revisited. Each entry notes the trade-off so future changes are informed.

---

## Vault Structure

### Subfolder mirroring (2026-04-18)
**Decision**: Root subdirectories of a registered project become vault subfolders. Files inside sub-subdirectories (depth 2+) are placed flat inside the nearest vault subfolder — they do NOT create further nesting.

Example: `AI/demo/src/api.py` → `Users-.../demo/api.md` (not `Users-.../demo/src/api.md`)

**Trade-off**: Keeps the vault shallow and browsable. Loses exact path context for deep files.

**To change**: Enable Q1-B (full recursion) in `scanner.py` and update `sync.py` accordingly.

---

### Note naming inside subfolders (2026-04-18)
**Decision (Q2-B)**: Notes inside vault subfolders are named after the file stem only (e.g., `api.py` → `api.md`), not the full relative path.

**Known limitation**: If two files within the same root subdir share a stem (e.g., `demo/index.js` and `demo/src/index.js`), the second write overwrites the first.

**To change**: Use relative-path-prefixed names (e.g., `src-api.md`) for files at depth 2+ within a subdir.

---

### Root index content (2026-04-18)
**Decision (Q3-B, provisional)**: The root `_index.md` lists all notes from all subdirs, grouped by subfolder. Each vault subfolder also gets its own `_index.md`.

**To change**: Switch to Q3-A (root index links only to subfolder indices) if the root index becomes too long.
