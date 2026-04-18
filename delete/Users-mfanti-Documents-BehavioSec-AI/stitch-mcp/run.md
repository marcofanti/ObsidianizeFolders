---
file_path: stitch-mcp/run.sh
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: sh
---

**Purpose**: Executes the complete development lifecycle for a local project within a specified directory.

**What it does**:
- Validates that a target directory is provided as a command-line argument.
- Changes the current working directory into the provided argument using `pushd`.
- Opens a web browser instance to the default development URL (`http://localhost:5173/`).
- Initiates the local development server using `npm run dev`.
- Ensures directory hygiene by restoring the original working directory using `popd` upon completion.

**Key exports**:
- None

**Gotchas**:
- The script assumes the presence of `npm` and that the project's `package.json` contains a valid `dev` script.
- The script uses `pushd` and `popd` to manage directory state; if the script fails before reaching `popd`, the working directory may be incorrectly left in the target project directory.
- The browser opening command (`open`) is specific to macOS; usage on other operating systems (like Linux) may require substituting it (e.g., `xdg-open`).