---
file_path: testclaude3/gemini-test/package-lock.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file is a lock file that precisely records the dependency tree and fixed versions of every package utilized by the `gemini-test` project, ensuring that subsequent installations are entirely reproducible across different environments.

**What it does**:
- Establishes a deterministic environment for package installation, eliminating dependency version drift.
- Defines the exact versions for core frontend libraries (React, React Router) and complex build tools (Vite, ESLint, TypeScript).
- Accounts for platform-specific binaries and optional dependencies (e.g., `lightningcss-darwin-x64`, `rolldown/binding-linux-x64-gnu`) to ensure compatibility across various operating systems and CPU architectures.

**Key exports**:
- `react` & `react-dom`: Provides the core reactive component model for the user interface.
- `react-router-dom`: Manages client-side routing and navigation within the application.
- `@auth0/auth0-*`: Implements specific client-side OAuth and authentication flows (Auth0 integration).
- `vite` & `@vitejs/plugin-react`: Acts as the primary development build tool and module bundler.
- `eslint`/`@typescript-eslint/*`: Enforces strict code quality, type checking, and linting rules across the codebase.

**Gotchas**:
- **Dependency Depth:** Due to the nature of a lock file, it is extremely verbose and describes an exhaustive dependency graph, making manual inspection difficult.
- **Platform Specificity:** The inclusion of numerous architecture-specific packages (`lightningcss-linux-arm64-gnu`, `rolldown/binding-darwin-x64`, etc.) indicates that the project build chain must correctly detect and pull binaries tailored to the host machine's OS and CPU.
- **Versioning Strictness:** The `engines` and `peerDependencies` sections enforce strict version requirements for Node.js and other related packages, meaning environment upgrades can easily break the project if not managed carefully.