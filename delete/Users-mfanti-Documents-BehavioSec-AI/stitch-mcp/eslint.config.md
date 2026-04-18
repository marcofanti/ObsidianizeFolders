---
file_path: stitch-mcp/real-estate/eslint.config.js
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: js
---

**Purpose**: Configures the ESLint static analysis tool to enforce coding standards and best practices for TypeScript, React, and modern JavaScript within the application source code.

**What it does**:
- Restricts linting analysis to files with `.ts` or `.tsx` extensions.
- Extends multiple rule sets to ensure compliance with standard JavaScript best practices, TypeScript type safety, React Hooks rules, and React component refreshing for Vite environments.
- Excludes the `dist` directory from linting analysis to prevent checking compiled build artifacts.
- Configures the environment to recognize standard browser global variables.

**Key exports**:
- `globalIgnores`: Ensures that the entire contents of the `dist` directory are skipped during linting.
- `js.configs.recommended`: Applies fundamental, recommended rules for modern JavaScript.
- `tseslint.configs.recommended`: Applies recommended rules and type checking best practices for TypeScript files.
- `reactHooks.configs.flat.recommended`: Enforces rules regarding the correct usage and dependency array management of React Hooks.
- `reactRefresh.configs.vite`: Applies specific rules necessary for integrating React components within a Vite build environment.

**Gotchas**:
- This configuration assumes the project uses the modern, flat config structure of ESLint (imported via `defineConfig`).
- The inclusion of `globals.browser` means that any global variables expected to exist in a standard browser environment (like `window` or `document`) are treated as defined, which can affect strict type checking if the project expects a specific Node.js environment.
- Because it includes `reactRefresh.configs.vite`, the source code should ideally be managed within a Vite-based build system.