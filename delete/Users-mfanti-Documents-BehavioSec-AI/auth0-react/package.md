---
file_path: auth0-react/package.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file defines the metadata, development environment, and build dependencies for a private React application utilizing the Auth0 authentication library.

**What it does**:
- Configures standard development workflows, including running the development server (`vite`), building the production assets (`tsc -b && vite build`), linting the code (`eslint .`), and previewing the resulting build (`vite preview`).
- Lists primary runtime dependencies required for a modern React application, including React and the `@auth0/auth0-react` package.

**Key exports**:
- `@auth0/auth0-react`: Provides the core React integration package for managing authentication flows with Auth0.
- `react` / `react-dom`: Core libraries for building the user interface using the React framework.
- `vite`: The modern build tool used to bundle and serve the application efficiently.

**Gotchas**:
- The project is marked as `"private": true`, indicating it is not intended for public consumption via package publication.
- The build process relies on two steps: TypeScript compilation (`tsc -b`) must complete before the Vite build step, ensuring type safety is checked before bundling.
- It utilizes a complex development stack, incorporating Vite, TypeScript, and comprehensive ESLint rules (including `react-hooks` and `react-refresh`) for robust code quality assurance.