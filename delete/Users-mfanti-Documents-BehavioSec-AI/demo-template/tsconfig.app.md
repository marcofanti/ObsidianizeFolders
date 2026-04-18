---
file_path: demo-template/finance-app/tsconfig.app.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Configures the TypeScript compiler for the application, enforcing strict type-checking rules while preparing the project for consumption by a modern build bundler.

**What it does**:
- Targets the application output to ES2020 standards using ESNext module resolution, ensuring compatibility with modern JavaScript environments.
- Enables strict type checking across the entire codebase, catching potential bugs at compile time.
- Treats source files as isolated modules, which is necessary when using modern bundlers (like Vite or Webpack).
- Specifies the React JSX runtime, indicating the framework used in the application.
- Crucially, it sets `noEmit: true`, meaning the compiler is used only for type validation, and an external build tool is responsible for generating the final JavaScript output.

**Gotchas**:
- Because `noEmit: true` is set, this configuration *only* validates types; the actual JavaScript bundling and file output must be handled by a separate tool (e.g., Vite, Webpack).
- The combination of `"strict": true` and several strict checks (e.g., `noUnusedLocals`, `noFallthroughCasesInSwitch`) means the codebase must adhere to very high standards of type safety and cleanliness.