---
file_path: demo-template/finance-app/tsconfig.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Specifies the configuration for multiple TypeScript projects within a workspace, referencing shared settings for the application and node environments.

**What it does**:
- Declares the root TypeScript configuration by referencing two child configuration files: `tsconfig.app.json` (likely for client-side application code) and `tsconfig.node.json` (likely for backend or utility code running in a Node environment).

**Key exports**:
- N/A

**Gotchas**:
- This file does not contain any compiler options itself; it solely manages the relationships between different configuration files in the project, requiring the existence and proper setup of the referenced files (`tsconfig.app.json` and `tsconfig.node.json`).