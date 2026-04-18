---
file_path: demo-to-chris-pre-built-bhs/finance-app/tsconfig.app.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Configures the TypeScript compiler options for the main application bundle, ensuring strict type checking and modern module resolution settings.

**What it does**:
- Sets the target JavaScript environment to ES2020, utilizing modern class field definitions (`useDefineForClassFields: true`).
- Configures module resolution for modern bundlers (`moduleResolution: "bundler"`) and specifies ESNext modules (`module: "ESNext"`).
- Enables highly strict type checking across the board (`strict: true`), enforcing checks for unused variables, parameters, and switch fallthrough cases.
- Treats the output as consumed by a bundler (setting `noEmit: true` and `isolatedModules: true`), preventing the compiler from generating physical output files directly, as a bundler will handle that process.

**Key exports**:
- None (This is a configuration file, not an exportable module).

**Gotchas**:
- Because `noEmit: true` and `isolatedModules: true` are set, this configuration assumes that a bundler (like Webpack or Vite) is responsible for compiling and emitting the final JavaScript files; the TypeScript compiler itself will not generate output.
- Setting `moduleResolution: "bundler"` is specific to modern build tooling and expects the source code structure to be resolved correctly by that tooling.
- The combination of `target: "ES2020"` and `lib: ["ES2020", "DOM", "DOM.Iterable"]` means the codebase is intended to run in a modern browser environment supporting these features.