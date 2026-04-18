---
file_path: demo-to-chris-pre-built-bhs/finance-app/package.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Defines the project configuration and dependencies for a React finance application using Vite and TypeScript.

**What it does**:
- Specifies development scripts (`dev`, `build`, `preview`) for running, compiling, and previewing the application.
- Lists necessary runtime dependencies (React, React DOM, React Router DOM) for the application to function.
- Defines development dependencies (TypeScript, Vite, and associated plugins/types) required for building and developing the project environment.

**Key exports**:
- None (This is a package configuration file, not an export module).

**Gotchas**:
- The project is configured to use modern module syntax (`"type": "module"`).
- The `build` script executes both a TypeScript compilation (`tsc -b`) and a Vite build (`vite build`), ensuring type safety and optimized production assets.