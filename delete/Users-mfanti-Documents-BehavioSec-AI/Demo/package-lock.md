---
file_path: Demo/package-lock.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file records the exact dependency tree and specific versions used for the project, ensuring reproducible builds across all environments.

**What it does**:
- Guarantees deterministic installation by listing the full dependency graph, including transitive dependencies (dependencies of dependencies).
- Stores cryptographic integrity hashes (`integrity`) and resolved URLs for every package, preventing unexpected dependency changes.
- Defines the specific major framework versions used (e.g., React 19.2.4, ESLint 9.39.4).

**Key exports**:
- **react**: Core React library for building user interfaces.
- **react-dom**: Provides the DOM rendering capabilities for React.
- **vite**: High-performance build tool and development server.
- **eslint**: Linter for enforcing coding standards and quality.
- **typescript**: Compile-time type checking and code transpilation.

**Gotchas**:
- **Do Not Edit Manually**: This file should be generated automatically by the package manager (`npm install`) and should not be manually edited.
- **Versioning Lock**: It strictly locks dependencies to specific versions, which means updating the stack requires explicitly modifying the `package.json` file and running the install command again.
- **Large Size**: Due to the sheer number of dependencies (including Babel and ESLint helper packages), the file is extensive and complex to debug.