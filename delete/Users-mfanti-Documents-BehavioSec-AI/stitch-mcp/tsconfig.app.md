---
file_path: stitch-mcp/banking/tsconfig.app.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file provides a highly configured TypeScript compiler environment definition for building a modern front-end application within a bundled build system (like Vite).

**What it does**:
- Configures the build to target the ES2023 standard and use the ESNext module system.
- Enforces maximum type safety using the `strict: true` setting and various linter rules.
- Optimizes for bundler usage by setting `moduleResolution: "bundler"` and `noEmit: true`, meaning the build process (not the compiler itself) is responsible for generating the final JavaScript files.
- Allows the use of modern React JSX syntax for component definition.

**Key exports**:
- target: Specifies the compiled JavaScript environment as ES2023.
- moduleResolution: Forces module resolution to use the specialized "bundler" mechanism, ensuring compatibility with modern build tools.
- jsx: Defines the compiler rules to handle React JSX syntax.

**Gotchas**:
- The combination of `"noEmit": true` and `"moduleResolution": "bundler"` dictates that the application must be compiled exclusively by a surrounding bundler (like Vite) and cannot be run standalone using `tsc` directly.
- The settings, particularly `verbatimModuleSyntax: true`, enforce extremely strict module imports, preventing type system ambiguities when importing modules.
- The file includes numerous aggressive linting rules (e.g., `noUnusedLocals`, `noUnusedParameters`) which, while beneficial for quality, require developers to rigorously clean up unused code paths.