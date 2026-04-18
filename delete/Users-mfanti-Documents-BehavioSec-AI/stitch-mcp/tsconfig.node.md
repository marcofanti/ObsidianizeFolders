---
file_path: stitch-mcp/gambling/tsconfig.node.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Configures the TypeScript compiler options for a modern, strict Node.js development environment, primarily intended for type checking within a bundler workflow.

**What it does**:
- Enforces extremely strict type safety across the codebase using compiler flags like `strict: true` and `noUncheckedSideEffectImports`.
- Sets the development target to modern JavaScript standards (ES2023) using `target: "ES2023"` and `lib: ["ES2023"]`.
- Configures the compiler specifically for use within modern build pipelines by setting `moduleResolution` to `"bundler"` and `noEmit: true`.
- Limits the scope of configuration and type checking exclusively to the `vite.config.ts` file.

**Gotchas**:
- The presence of `"noEmit": true` indicates that this `tsconfig` is strictly for type checking and linting, not for generating compiled JavaScript output; actual compilation must be handled by a bundler (like Vite).
- The use of `"moduleResolution": "bundler"` requires the project to be integrated with a bundler that supports this modern module resolution strategy.