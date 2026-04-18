---
file_path: demo-to-chris-pre-built/gemini-test/eslint.config.js
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: js
---

**Purpose**: Configures a comprehensive and flat linting rule set for a modern JavaScript/TypeScript project using ESLint.

**What it does**:
- Applies recommended rulesets from core ESLint, TypeScript, React Hooks, and React Refresh plugins.
- Targets all files ending in `.ts` or `.tsx` within the project.
- Defines JavaScript runtime rules using `ecmaVersion: 2020` and includes browser-specific global variables.
- Excludes the `dist` directory from all linting checks using `globalIgnores`.

**Key exports**:
- default: The resulting ESLint configuration object, which aggregates multiple linting rules into a single cohesive setup.

**Gotchas**:
- It uses the modern flat configuration format (`@eslint/config`), which requires importing specific configurations (e.g., `js.configs.recommended`).
- The inclusion of `reactHooks.configs.flat.recommended` and `reactRefresh.configs.vite` implies that the project structure and build tool are likely utilizing React hooks and a Vite build pipeline.
- The `globalIgnores(['dist'])` must be placed at the beginning of the array to ensure it applies globally before file-specific rulesets are processed.