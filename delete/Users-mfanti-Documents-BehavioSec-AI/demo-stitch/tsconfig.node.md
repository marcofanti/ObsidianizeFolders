---
file_path: demo-stitch/tsconfig.node.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file configures TypeScript to strictly type-check a Node-specific configuration file (`vite.config.ts`) without generating output JavaScript code.

**What it does**:
- Enables the strictest possible type checking across the project.
- Configures the compiler for modern bundling environments using ES modules (ESNext, `moduleResolution: "bundler"`).
- Ensures type validation is performed only on the specified build configuration file.
- Prevents the compiler from emitting any JavaScript files (`"noEmit": true`).

**Key exports**:
- (No explicit exports are defined; this file is a compiler configuration defining how the project's entry points are processed.)

**Gotchas**:
- The combination of `"noEmit": true` and `"strict": true` means that if there are any type errors or unused variables within the included files, the build process will fail immediately, even if the code would run correctly at runtime.
- The settings heavily prioritize type safety and compatibility with modern bundling tools (like Vite/Rollup) over general compilation flexibility.