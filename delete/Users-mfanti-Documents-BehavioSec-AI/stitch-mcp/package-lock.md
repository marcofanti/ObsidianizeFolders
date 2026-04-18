---
file_path: stitch-mcp/retail/package-lock.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file locks the precise version and integrity hash of every package and sub-dependency required by the project, ensuring deterministic builds across different environments.

**What it does**:
- Records the entire dependency graph for the `retaildemo` application.
- Specifies the exact versions of primary dependencies (e.g., `react`, `react-dom`, `react-router-dom`).
- Defines the full toolchain for development, including build utilities (`vite`), styling processors (`tailwindcss`, `postcss`, `autoprefixer`), and code linters/type checkers (`eslint`, `typescript`).

**Key exports**:
- `react`: The core library for building user interfaces with components.
- `react-dom`: Provides the renderer for React components into the DOM.
- `react-router-dom`: Handles client-side routing within the React application.
- `vite`: A modern build tool and development server used for bundling and hot module replacement.
- `tailwindcss`: A utility-first CSS framework for styling the application.
- `typescript`: Used for static type checking and development, providing strong typing benefits.
- `eslint`: The standard tool for linting code and enforcing quality standards.

**Gotchas**:
- **Size and Complexity**: The file is extremely large due to its comprehensive recording of every minor dependency, including all Babel and ESLint helper packages, which is normal for a modern JS stack but signals deep dependency tracking.
- **Dev Dependencies**: The overwhelming majority of packages listed are development (`dev: true`) and build-time tools, indicating this is a project structure file, not a runtime bundle.
- **Versioning**: The presence of major dependencies like React (19.2.4) and Vite (8.0.1) suggests the project utilizes very recent or pre-release versions of foundational frameworks.
- **Platform Bindings**: The inclusion of numerous packages under `@rolldown/binding-*` and similar bindings demonstrates the toolchain's effort to support specific operating systems and architectures (e.g., `darwin-arm64`, `linux-x64-gnu`, `win32-arm64-msvc`), which is typical for advanced build tooling.