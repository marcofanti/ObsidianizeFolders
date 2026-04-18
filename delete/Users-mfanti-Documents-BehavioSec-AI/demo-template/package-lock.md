---
file_path: demo-template/finance-app/package-lock.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file records the complete, deterministic dependency tree and exact version mappings used by the project, ensuring repeatable installations across different environments.

**What it does**:
- Locks all dependencies (both `dependencies` and `devDependencies`) to specific, resolved versions and integrity hashes (SHAs).
- Guarantees that running `npm install` will install the identical set of packages regardless of when or where the command is executed.
- Details the specific `node_modules` structure, including local package versions and required dependencies for complex tools like Babel and Vite.

**Key exports**:
*   **react**: Core React library for building user interfaces.
*   **react-dom**: React bindings for the browser environment.
*   **react-router-dom**: Library for client-side routing in React applications.
*   **typescript**: Tools and definitions for writing type-safe JavaScript.
*   **vite**: Modern build tool/development server.

**Gotchas**:
- **Size and Complexity**: The file is extremely verbose and large because it contains the entire dependency tree (including dozens of Babel helper modules and platform-specific `esbuild` builds).
- **Never Manually Edit**: This file should *only* be managed by package manager commands (e.g., `npm install`, `npm update`). Manual editing can break the lock, leading to non-reproducible builds.
- **Build Tool Dependencies**: It shows an exhaustive list of development dependencies and platform-specific builds (e.g., `@esbuild/linux-x64`, `rollup-linux-arm-musl`) necessary for modern bundlers like Vite and Rollup to compile for various target architectures.