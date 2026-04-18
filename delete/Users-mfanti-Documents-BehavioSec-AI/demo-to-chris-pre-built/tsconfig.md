---
file_path: demo-to-chris-pre-built/finance-app/tsconfig.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This configuration file aggregates and references the TypeScript compiler options for the entire application, splitting compiler settings for the main client-side application logic and the separate Node.js backend/environment.

**What it does**:
- It defines the compilation scope for the entire project by pointing to two specialized configuration files: one for client-facing code (`tsconfig.app.json`) and one for backend code running in a Node environment (`tsconfig.node.json`).

**Key exports**:
- `tsconfig.app.json`: Contains the TypeScript compilation options specific to the main application (likely client-side or browser-based code).
- `tsconfig.node.json`: Contains the TypeScript compilation options specifically for code running in a Node.js environment (e.g., server routes, utilities).

**Gotchas**:
- This file does not define any compiler settings itself; it is purely a container that links the project to its specialized configuration files.
- If a user needs to change the build rules for the application or the Node environment, they must modify the referenced files (`tsconfig.app.json` or `tsconfig.node.json`), not this root file.
- The structure mandates that the compiler treat the application build and the Node build as distinct compilation units.