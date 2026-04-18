---
file_path: stitch-mcp/.claude/settings.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file configures the explicit operational permissions, allowed bash commands, and recognized file directories for the agent or system utilizing the Claude environment.

**What it does**:
- Grants permission to execute the standard project build script (`npm run build`).
- Enables network capability to check the HTTP status code of a local development server running on port 5174.
- Allows invocation of internal project management functions, including project creation and screen generation from text.
- Permits the execution of system commands required to terminate a running 'vite' process.
- Explicitly registers a non-standard user directory (`/Users/mfanti/.gemini/antigravity`) for system access.

**Gotchas**:
- **High Privilege Scope**: The configured permissions allow powerful actions, including running build scripts, making external network calls, and killing arbitrary processes, making the system highly capable but requires trust in the source of the configuration.
- **Environment Specificity**: The included paths and commands are hardcoded and rely on the specific local environment setup (e.g., the user path `/Users/mfanti/` and the assumption that `vite` is the process to be killed).