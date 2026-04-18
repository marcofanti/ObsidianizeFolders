---
file_path: testclaude3/gemini-test/tsconfig.node.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file configures the TypeScript compiler environment to enforce maximum type safety and modern module resolution specifically for build tooling configuration files.

**What it does**:
- Establishes a highly restrictive development environment by enabling `strict: true` and various specific checks (e.g., `noUnusedLocals`, `noUncheckedSideEffectImports`).
- Uses the "bundler" module resolution strategy, optimizing the project for modern bundlers (like Vite) rather than traditional compilation paths.
- Configures the compiler to function purely as a type checker by setting `"noEmit": true`, ensuring that type errors fail the build without generating incomplete JavaScript files.

**Gotchas**:
- Because `"noEmit": true` and `"strict": true` are set, any type error or linting violation will halt the build process and must be manually corrected before successful compilation, as no output files are generated.
- The strict module configuration (`moduleResolution: "bundler"`, `verbatimModuleSyntax: true`) requires the project to adhere strictly to modern ES module standards, making compatibility with older module formats difficult.