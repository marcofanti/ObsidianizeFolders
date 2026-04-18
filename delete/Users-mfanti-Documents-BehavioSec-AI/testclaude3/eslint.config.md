---
file_path: testclaude3/gemini-test/eslint.config.js
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: js
---

**Purpose**: This file configures the ESLint linter using the flat config format to enforce standardized best practices for TypeScript, React, and general JavaScript code within a project.

**What it does**:
- Configures the linter to ignore files within the `dist` directory.
- Applies a comprehensive set of rules (including recommended best practices, TypeScript rules, React Hooks rules, and React Refresh rules) specifically to files matching the `**/*.{ts,tsx}` pattern.
- Sets the JavaScript environment to ES2020 and includes standard browser global variables for linting.

**Key exports**:
- `default`: Exports the main ESLint configuration array, defining all rulesets and scopes for the linter.

**Gotchas**:
- **Flat Config Format:** It utilizes the modern ESLint flat config system (`@eslint/config`), which is significantly different from previous, object-based configurations.
- **Specific Scoping:** The ruleset for React and TypeScript is explicitly scoped to `files: ['**/*.{ts,tsx}']`; applying rules outside this scope will ignore these specific plugins/rules.
- **Plugin Order/Conflict:** Since it extends multiple rule sets (`js.configs.recommended`, `tseslint.configs.recommended`, etc.), conflicts or overly strict rules can sometimes arise, requiring careful management of the included plugins.