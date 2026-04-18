---
file_path: demo-stitch/package.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Defines the metadata, script commands, and required dependencies for building and running a modular React-based financial application.

**What it does**:
- Runs a development server using Vite for live hot-reloading during development (`npm run dev`).
- Executes a full build process that first compiles TypeScript (`tsc -b`) and then bundles the application assets (`vite build`).
- Serves the finished production build for local previewing after the build process is complete.
- Includes a dedicated script for running project-specific validation logic (`npm run validate`).

**Key exports**:
- dev: Starts the local development environment using Vite.
- build: Executes the full build lifecycle, compiling TypeScript and bundling the code.
- preview: Starts a local server to test the production build.
- validate: Runs a dedicated Node script for project validation checks.

**Gotchas**:
- The project is marked as `"private": true`, meaning it is intended for local use and should not be published to a public package registry.
- The build process explicitly chains TypeScript compilation (`tsc -b`) before running Vite, ensuring type safety checks run as part of the standard build command.
- It uses a modular JavaScript environment (`"type": "module"`).