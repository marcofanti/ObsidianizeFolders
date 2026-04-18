---
file_path: Demo/package.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Defines the metadata, dependencies, and standardized scripts for a private, module-based React application initialized with Vite and TypeScript.

**What it does**:
- Enables standard development lifecycle commands: `dev` starts the local development server using Vite; `build` compiles the project using TypeScript and bundles it with Vite; `lint` checks code quality using ESLint; and `preview` serves the built application for testing.

**Key exports**:
- react: The primary JavaScript library for building user interfaces.
- react-dom: Provides DOM-specific methods and rendering capabilities for React.

**Gotchas**:
- The project is marked as `private: true`, meaning it is intended for local use and cannot be published to public package registries.
- The build process is explicit and two-phased: `tsc -b` runs TypeScript compilation first, followed by `vite build` for bundling.
- The `type: "module"` setting indicates that the project uses ES module syntax throughout.