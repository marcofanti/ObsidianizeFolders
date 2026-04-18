---
file_path: Demo/tsconfig.node.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Configures the TypeScript compiler options for type-checking and linting Node.js environment files, specifically tailored for modern bundler workflows.

**What it does**:
- Enables the use of modern JavaScript features up to ES2023.
- Enforces strict type checking, unused code detection, and exhaustive switch statements.
- Treats the project as if it is being handled by a bundler, allowing advanced module syntax (`moduleResolution: "bundler"`).
- Ensures the compiler does not generate output JavaScript files (`noEmit: true`), restricting its function to pure type validation.

**Key exports**:
- `moduleResolution: "bundler"`: Forces the compiler to resolve modules according to modern bundler standards.
- `noEmit: true`: Guarantees that TypeScript performs only type checking and does not output compiled JavaScript files.
- `include`: Specifies that only `vite.config.ts` is processed by this configuration.

**Gotchas**:
- Since `noEmit: true` is set, this file is strictly for development-time type validation and linting, and *will not* compile the source code into runnable JavaScript files itself.
- The combination of `"module": "ESNext"` and `"moduleResolution": "bundler"` dictates a highly modern module environment, requiring all consuming code to adhere to ES module standards.