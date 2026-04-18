---
file_path: demo-to-chris-pre-built/finance-app copy/tsconfig.app.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Configures the TypeScript compiler options for the application source files, enabling strict type checking and modern module resolution for a bundler environment.

**What it does**:
- Enforces strict type checking and linter rules across all files included in the `src` directory.
- Targets modern JavaScript features (`ES2020`, `ESNext`) and uses `react-jsx` for JSX syntax.
- Sets up the compiler to resolve modules using a `bundler` system, which is standard practice for modern front-end build tools.
- Confirms that the compiler should only validate types and not generate JavaScript output (`"noEmit": true`).

**Key exports**:
- (N/A - This is a configuration file, not a module exporting defined symbols.)

**Gotchas**:
- The combination of `"noEmit": true`, `"isolatedModules": true`, and `"moduleResolution": "bundler"` indicates this file is designed to run within a modern build pipeline (like Vite or Next.js), where the actual transpilation and bundling process are handled by the build tool, and TypeScript's role is solely type validation.
- Using `"strict": true` means the code must adhere to the highest level of type safety, potentially failing on older or less strictly typed codebases.