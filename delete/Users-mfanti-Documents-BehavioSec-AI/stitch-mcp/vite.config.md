---
file_path: stitch-mcp/banking/vite.config.ts
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: ts
---

**Purpose**: Configures the Vite build environment for the React frontend application within the banking module.

**What it does**:
- Initializes the Vite build system using `defineConfig`.
- Registers the `@vitejs/plugin-react` plugin, enabling proper handling of React-specific features like JSX and Fast Refresh during development and build.

**Key exports**:
- default: The main Vite configuration object, containing the plugin array.

**Gotchas**:
- This file only defines plugins and does not configure any specific build options (e.g., `build` output targets, `server` port, or `resolve` aliases). Any advanced environment setup must be added to the exported object.