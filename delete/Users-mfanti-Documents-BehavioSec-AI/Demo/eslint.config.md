---
file_path: Demo/eslint.config.js
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: js
---

**Purpose**: Configures a comprehensive and modern ESLint ruleset tailored for TypeScript, React, and Vite environments.

**What it does**:
- Applies general recommended rulesets for JavaScript, TypeScript, React Hooks, and React Refresh.
- Excludes the `dist` directory from linting checks.
- Targets files with the `.ts` and `.tsx` extensions, ensuring type safety checks are enforced.
- Sets the JavaScript environment to ES2020 and recognizes standard browser global variables.

**Key exports**:
- Configuration Array: Exports a structured array containing all the combined ESLint rules, defined by `defineConfig`.

**Gotchas**:
- This configuration relies on the modern flat configuration format (`eslint/config`).
- It is highly opinionated; users must ensure `eslint-plugin-react-hooks` and `eslint-plugin-react-refresh` are installed to properly validate React code.
- The `globalIgnores(['dist'])` line ensures that generated output files are not linted, which is crucial for build processes.