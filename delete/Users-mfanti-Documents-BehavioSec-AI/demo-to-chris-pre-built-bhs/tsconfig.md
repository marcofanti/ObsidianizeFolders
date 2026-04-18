---
file_path: demo-to-chris-pre-built-bhs/finance-app/tsconfig.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: To serve as a root configuration file that aggregates and manages TypeScript compiler options for the entire `finance-app`.

**What it does**:
- It does not define any compiler options itself, relying entirely on the `references` field.
- It establishes relationships between the root configuration and specific sub-configurations for application code and backend/node scripts, ensuring all parts of the project adhere to standardized TypeScript settings.

**Key exports**:
- `tsconfig.app.json`: Configures the TypeScript settings specifically for the main application code/client side.
- `tsconfig.node.json`: Configures the TypeScript settings specifically for Node.js scripts, backend services, or tooling scripts.

**Gotchas**:
- This file's purpose is purely structural (reference management); it contains no actual compiler settings (evidenced by `files: []`).
- Changes to configuration options must be made within the referenced files (`tsconfig.app.json` or `tsconfig.node.json`), not directly in this root `tsconfig.json`.