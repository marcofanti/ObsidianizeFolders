---
file_path: demo-stitch/tsconfig.app.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Configures the TypeScript compiler for the application build, enforcing strict type checking and optimizing the module resolution for modern JavaScript bundlers.

**What it does**:
- Specifies that the compiler should not generate JavaScript output (`noEmit: true`), meaning this file is used solely for type checking.
- Enforces the highest level of type safety using `strict: true` and various unused code checkers.
- Targets a modern JavaScript environment (`ES2020`) while providing necessary browser definitions (`DOM`).
- Optimizes the module system for use with bundlers (e.g., Vite/Webpack) by setting `isolatedModules: true` and `moduleResolution: "bundler"`.
- Configures support for React JSX syntax.

**Key exports**:
- JSX: Enables React JSX transform (`react-jsx`).
- Targeting: Compiles code using modern JavaScript features (`ES2020`).
- Type Checking: Enforces maximum type safety across the codebase (`strict: true`).

**Gotchas**:
- **No Output:** Because `noEmit: true` is set, the compiler will only validate types and will not generate the resulting JavaScript files; a separate build step (like a bundler) is required to output the code.
- **Strictness:** The combination of `strict: true` and multiple unused checks enforces a very high bar for code quality, and developers must ensure all variables and parameters are used or explicitly marked as unused.
- **Isolated Modules:** Setting `isolatedModules: true` means that each file is treated as an independent module, which is standard for bundlers but might prevent certain types of ambient or global type usage patterns.