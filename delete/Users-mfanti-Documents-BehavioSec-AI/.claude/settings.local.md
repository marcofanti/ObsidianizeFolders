---
file_path: .claude/settings.local.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This configuration file restricts and defines the specific shell commands and filesystem accesses that an associated AI agent is authorized to run.

**What it does**:
- Allows the agent to search for and list the first 20 source code files (`.tsx`, `.jsx`, `.ts`, `.js`) within the `/Users/mfanti/Documents/BehavioSec/AI` directory.
- Allows the agent to search for and list the first 20 `package.json` files within the `/Users/mfanti/Documents/BehavioSec/AI` directory, excluding those found in `node_modules`.
- Permits the execution of a specific dependency installation command (`npm install @auth0/auth0-react`) within the `auth0-react` subdirectory.

**Gotchas**:
- All executed permissions rely on hardcoded, absolute file paths specific to the local machine (`/Users/mfanti/...`), making this configuration non-portable.
- The file uses `| head -20` on both file search commands, meaning that the agent will only retrieve and report the first 20 matching files, regardless of how many files actually exist in the target directory.
- The permissions are highly granular and restrictive; the agent cannot perform arbitrary shell commands outside of the explicitly defined `Bash()` functions.