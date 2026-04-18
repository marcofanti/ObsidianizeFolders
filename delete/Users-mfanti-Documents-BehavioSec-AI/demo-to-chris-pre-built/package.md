---
file_path: demo-to-chris-pre-built/finance-app copy/package.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Defines the metadata, dependencies, and build scripts for a modern single-page application using React and TypeScript.

**What it does**:
- Allows running the application in development mode via `vite`.
- Executes a full build process that first types checks the code with TypeScript (`tsc -b`) and then bundles the result using Vite (`vite build`).
- Provides a preview script (`vite preview`) for serving the built assets locally.

**Key exports**:
- react: Core library for building user interfaces.
- react-dom: Provides DOM-specific methods for React.
- react-router-dom: Handles client-side routing for the application.
- vite: The build tool used to bundle and serve the application.
- typescript: TypeScript compiler used for static type checking.

**Gotchas**:
- The build command (`"build": "tsc -b && vite build"`) requires TypeScript to run the type checking *before* Vite attempts the bundling, which is a crucial two-step process.
- This application is designed as a client-side SPA, using `react-router-dom` for navigation.
- The `type: "module"` setting indicates that the project uses ES module syntax.