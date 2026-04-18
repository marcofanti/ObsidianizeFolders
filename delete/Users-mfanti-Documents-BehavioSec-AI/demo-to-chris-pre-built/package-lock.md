---
file_path: demo-to-chris-pre-built/gemini-test/package-lock.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file is a lock file detailing the exact version and dependency tree for the `gemini-test` project, ensuring reproducible package installations.

**What it does**:
- Defines all required runtime dependencies (`react`, `react-dom`, `react-router-dom`, `lucide-react`) and development dependencies (`typescript`, `eslint`, `vite`, various Babel and ESLint utility packages).
- Specifies the exact versions of all transitive dependencies (e.g., various `@babel/` packages, `eslint` components, etc.) to guarantee build stability across different environments.

**Key exports**:
- *None (This is a lockfile, not a module that exports functionality)*

**Gotchas**:
- **Massive Dependency Graph**: The lock file contains a huge number of deeply nested dependencies (especially Babel and ESLint utilities), indicating a complex modern frontend setup.
- **Development Focus**: The heavy inclusion of `@eslint/*`, `typescript-*`, and `vite` packages confirms that this project uses TypeScript and ESLint for robust linting and development tooling.
- **Version Drift**: Due to the sheer volume of dependencies, updating or resolving conflicts can be complex; relying on this lock file is critical for CI/CD environments.