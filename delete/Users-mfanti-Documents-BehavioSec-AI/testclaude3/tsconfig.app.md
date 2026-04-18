---
file_path: testclaude3/gemini-test/tsconfig.app.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Configures the TypeScript compiler and associated build tools for a modern, type-safe application build environment.

**What it does**:
- Sets the target environment to ES2023 and uses modern module standards (`ESNext`, `moduleResolution: "bundler"`).
- Enables the React Fast Refresh JSX transform (`jsx: "react-jsx"`).
- Enforces an extremely strict type-checking environment with options like `strict`, `noUnusedLocals`, and `noUncheckedSideEffectImports`.
- Instructs the compiler to perform type checking and resolve module paths without emitting actual JavaScript files (`"noEmit": true`).
- Specifies that source files within the `src` directory should be included in the compilation scope.

**Key exports**:
- `src`: Defines the root directory for source files that TypeScript should process.

**Gotchas**:
- **Type Checking vs. Compilation**: Since `"noEmit": true` is set, this configuration is primarily used for type checking and development environment tooling (like IDE/bundler linting), and will not produce runnable JavaScript output on its own.
- **Strictness**: The configuration enforces very strict typing rules (e.g., `"noUnusedLocals": true`), meaning code that relies on unused variables or parameters will fail type checks.
- **Module Resolution**: Using `"moduleResolution": "bundler"` requires all imports to be resolved efficiently by modern module bundlers.