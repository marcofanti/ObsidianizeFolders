---
file_path: auth0-react/tsconfig.node.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Configures the TypeScript compiler to enforce strict type checking and linting rules for a Node.js environment without generating any compiled JavaScript output.

**What it does**:
- Enables modern JavaScript features by targeting `ES2023` and using `ESNext` modules, optimized for bundler consumption.
- Ensures high type safety and compliance using the `strict` mode and several granular linter flags (e.g., `noUnusedLocals`, `noFallthroughCasesInSwitch`).
- Explicitly prevents the compiler from emitting output JavaScript files (`"noEmit": true`), indicating this configuration is used solely for type checking and validation.

**Gotchas**:
- Because `noEmit` is set to `true`, this configuration will only validate types; the resulting directory will not contain compiled JS files.
- The high level of strictness (e.g., `verbatimModuleSyntax: true`, `noUncheckedSideEffectImports: true`) means that any deviation from best practices or complex module import usage will cause the type check to fail.
- This configuration is specifically tailored for use in a bundler context (like Vite) rather than for standalone TypeScript compilation.