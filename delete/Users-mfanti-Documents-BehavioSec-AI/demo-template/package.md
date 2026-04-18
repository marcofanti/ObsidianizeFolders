---
file_path: demo-template/finance-app/package.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Configures the development environment, dependencies, and build scripts for a single-page React application using TypeScript and Vite.

**What it does**:
- Defines three primary lifecycle scripts: `dev` (runs the development server), `build` (compiles TypeScript and bundles the app for production), and `preview` (serves the optimized built application).
- Specifies core runtime dependencies for the application, including React, ReactDOM, and React Router DOM.
- Manages development tools (devDependencies), such as TypeScript, Vite, and React plugins, necessary for compiling and running the project locally.

**Key exports**:
- `react`: Provides the primary library for building the user interface components.
- `react-router-dom`: Handles client-side routing and navigation within the single-page application.
- `vite`: Serves as the build tool and development server, optimizing the build process.

**Gotchas**:
- The `"private": true` flag indicates that this package is not intended to be published to the npm registry.
- The `"type": "module"` setting requires all JavaScript imports/exports to use ES Module syntax (e.g., `import ... from '...'`).
- The `build` script enforces a strict build process (`tsc -b`) before bundling, ensuring type correctness before packaging the production assets.