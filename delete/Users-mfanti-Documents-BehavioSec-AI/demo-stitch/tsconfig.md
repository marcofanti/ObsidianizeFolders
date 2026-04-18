---
file_path: demo-stitch/tsconfig.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file acts as a root configuration pointer, instructing the TypeScript compiler to use and combine settings from separate application and node environment configuration files.

**What it does**:
- It defines the project structure by referencing two distinct, specialized TypeScript configuration files (`tsconfig.app.json` and `tsconfig.node.json`).
- It ensures that the compiler correctly understands the dependencies and configurations for both the main application code and any Node-specific backend logic within the project.

**Key exports**:
- `tsconfig.app.json`: Provides the configuration rules for the application's client-side or primary runtime environment.
- `tsconfig.node.json`: Provides the configuration rules specific to backend or command-line scripts that execute in a Node.js environment.

**Gotchas**:
- This file does not contain any actual compiler options (like `target` or `moduleResolution`); its sole purpose is to aggregate and manage multiple, separate configuration files defined in the project.
- Changes to any referenced file (`tsconfig.app.json` or `tsconfig.node.json`) will affect the project build, even if this root file is not modified.