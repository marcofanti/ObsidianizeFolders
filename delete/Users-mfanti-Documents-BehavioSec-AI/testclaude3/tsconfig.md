---
file_path: testclaude3/gemini-test/tsconfig.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file acts as a root TypeScript compiler reference, aggregating and defining the compilation settings for both the application client and the Node environment within the project.

**What it does**:
- Establishes a compilation dependency graph, ensuring that the TypeScript compiler processes the configurations defined in the referenced `tsconfig.app.json` and `tsconfig.node.json` files in the correct order.

**Key exports**:
- `tsconfig.app.json`: Defines the root compilation settings used for the primary application code.
- `tsconfig.node.json`: Defines the root compilation settings used specifically for backend or Node.js-related code.

**Gotchas**:
- The file itself contains no compilation options (`files: []`) and is purely structural; it must be referenced by the build tool to function correctly.
- Using `references` is crucial in multi-module or monorepo setups, as it forces the compiler to compile dependencies (the referenced projects) before attempting to compile the current project.