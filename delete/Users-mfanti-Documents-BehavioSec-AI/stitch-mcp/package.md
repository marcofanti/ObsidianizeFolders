---
file_path: stitch-mcp/logisticsdemo/package.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file defines the metadata, required dependencies, and build scripts for a client-side React application named `logisticsdemo`.

**What it does**:
- Provides standardized scripts for developing (`vite`), building the production assets (`tsc -b && vite build`), linting (`eslint .`), and locally previewing the application.
- Configures the project to use React, React Router, TypeScript, and Tailwind CSS for component definition and styling.

**Gotchas**:
- The presence of `private: true` indicates that this package is not intended to be published to a package registry.
- The `build` script utilizes both TypeScript compilation (`tsc -b`) and Vite bundling, ensuring type safety before asset creation.