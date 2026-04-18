---
file_path: demo-stitch/src/vite-env.d.ts
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: ts
---

**Purpose**: This file is a declaration file used to integrate Vite-specific type definitions into the TypeScript compiler, ensuring type safety across the development environment.

**What it does**:
- Includes all type definitions provided by the `vite/client` module via a reference directive.
- Makes Vite-specific global variables, functions, and types (such as module resolver types) available for use throughout the consuming code base.

**Gotchas**:
- This file is highly dependent on the project utilizing Vite for bundling and development; its contents must not be modified if the build tool changes.
- It is critical for proper type inference; if the application structure changes or Vite is upgraded, developers should verify that the referenced types remain accurate.