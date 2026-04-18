---
file_path: testclaude3/gemini-test/package.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file configures a React application environment, managing scripts, dependencies, and build tools for development and production deployment.

**What it does**:
- Defines common scripts for development (`dev`), production builds (`build`), code quality checks (`lint`), and local previewing (`preview`).
- Specifies required runtime dependencies, including React, React Router, and Auth0 integration.
- Lists development dependencies, which include TypeScript, ESLint, Vite, and React-specific type definitions, used solely for building and maintaining the code structure.

**Key exports**:
- `dev`: Runs the project using Vite for a local development server.
- `build`: Executes type checking (`tsc -b`) followed by the Vite build process, creating optimized production assets.
- `lint`: Runs ESLint to enforce code quality and style across the project.
- `preview`: Serves the optimized, built application locally for testing.

**Gotchas**:
- The project uses `type: "module"`, indicating that all JavaScript modules should be treated as ES Modules.
- It is configured for React 19 and TypeScript v5, suggesting the need for recent versions of tooling to avoid compatibility issues.
- The file is marked `"private": true`, implying this package should not be published to a public registry.