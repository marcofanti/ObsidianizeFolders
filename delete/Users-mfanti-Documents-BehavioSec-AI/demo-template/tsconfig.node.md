---
file_path: demo-template/finance-app/tsconfig.node.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Configures the TypeScript compiler for strict compile-time type checking, specifically for build tools (like Vite) that handle module resolution but do not require JavaScript file output.

**What it does**:
- Targets modern JavaScript standards (ES2022/ES2023) using a bundler-friendly module resolution strategy.
- Enforces the strictest set of TypeScript rules (`strict: true`, `noUnusedLocals`, etc.) to catch potential development errors during compilation.
- Ensures that the compiler only performs checks and does not generate any final JavaScript files (`"noEmit": true`).
- Limits the scope of the configuration only to `vite.config.ts`.

**Gotchas**:
- Because `"noEmit": true` is set, this configuration is designed purely for *type checking* and *tooling* (e.g., running a build script), and will not compile or emit a JavaScript output bundle itself.
- The combination of `"isolatedModules": true` and `"moduleResolution": "bundler"` is necessary for modern tooling that processes files in parallel or independently.