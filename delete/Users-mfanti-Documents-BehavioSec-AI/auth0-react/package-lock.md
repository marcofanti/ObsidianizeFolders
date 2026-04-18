---
file_path: auth0-react/package-lock.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file records the specific, locked dependency tree for the `auth0-react` package, ensuring reproducible builds across all environments.

**What it does**:
- Specifies the exact versions and integrity hashes for every direct and transitive dependency (e.g., React, ESLint, Babel, and internal Auth0 modules).
- Differentiates between runtime dependencies (`dependencies`) and development/build-time tooling (`devDependencies`).
- Provides a highly detailed manifest of the entire component ecosystem required for the package to function correctly.

**Key exports**:
- **`@auth0/auth0-react`**: The primary React component library for integrating Auth0 authentication flow into a modern React application.
- **`@auth0/auth0-spa-js`**: Core JavaScript logic for handling the authentication flow and token management in single-page applications.
- **`react` / `react-dom`**: The underlying React rendering and state management libraries used by the component.
- **`eslint` / `typescript-*`**: A comprehensive set of tools and type definitions used for linting, code quality checking, and type safety during development.

**Gotchas**:
- **Operational File:** This file is a machine-generated manifest and should never be manually edited. It must be committed to source control to guarantee that all contributors use the identical set of dependencies.
- **Version Pinning:** All versions listed (e.g., React `^19.2.4`) are strictly pinned by the integrity hashes (`sha512:...`), meaning any necessary upgrade or change to a dependency requires regenerating and committing this file.
- **Complexity:** The lock file includes an extensive list of development-only tools (like Babel, ESLint, `lightningcss`, `rolldown`, and various polyfills) that are necessary for the build process but are not part of the public API.