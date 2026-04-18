---
file_path: Demo/README.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document provides setup instructions and configuration recommendations for a minimal React application scaffold built using Vite and TypeScript.

**What it does**:
- Sets up a basic environment for React development with Hot Module Replacement (HMR) and ESLint rules.
- Outlines how to choose between different `@vitejs/plugin-react` versions (Oxc or SWC).
- Provides explicit guidelines for upgrading ESLint configurations to enable type-aware linting for production applications.
- Demonstrates how to integrate dedicated `eslint-plugin-react-x` and `eslint-plugin-react-dom` for enhanced React-specific linting.

**Key exports**:
- `@vitejs/plugin-react` / `@vitejs/plugin-react-swc`: Official Vite plugins used to compile React components, supporting different underlying tools (Oxc or SWC).
- `tseslint.configs.recommendedTypeChecked` / `tseslint.configs.strictTypeChecked`: Recommended type-aware ESLint configurations for production use.
- `eslint-plugin-react-x` / `eslint-plugin-react-dom`: Specialized ESLint plugins for enforcing specific rules related to React context and DOM usage.

**Gotchas**:
- The React Compiler is explicitly *not* enabled in this template due to potential negative impacts on development and build performance.
- For production, developers must manually update the ESLint configuration, replacing basic configs with `tseslint.configs.recommendedTypeChecked` or `tseslint.configs.strictTypeChecked` to ensure type safety during linting.
- Using `eslint-plugin-react-x` and `eslint-plugin-react-dom` requires updating both the `extends` array and ensuring proper `tsconfig.json` definitions are included in `languageOptions.parserOptions` for correct project resolution.