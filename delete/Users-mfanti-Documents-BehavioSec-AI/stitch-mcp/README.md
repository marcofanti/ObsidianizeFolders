---
file_path: stitch-mcp/logisticsdemo/README.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file provides a technical guide and setup instructions for initializing a React application using TypeScript and Vite, focusing on optimal linting configurations.

**What it does**:
- Establishes a minimal boilerplate setup for React development in Vite with Hot Module Replacement (HMR) and ESLint rules.
- Recommends using `tseslint.configs.recommendedTypeChecked` or `tseslint.configs.strictTypeChecked` to enable type-aware linting for production applications.
- Provides structured code examples for integrating advanced ESLint configurations, including type checking and specialized React plugins (`eslint-plugin-react-x` and `eslint-plugin-react-dom`).

**Key exports**:
- `@vitejs/plugin-react`: Official plugin for Vite enabling React support, available in variants using Oxc or SWC.
- `tseslint.configs.recommendedTypeChecked` / `tseslint.configs.strictTypeChecked`: Recommended configurations used to enhance ESLint by integrating full type checking into lint rules.
- `eslint-plugin-react-x` / `eslint-plugin-react-dom`: Specialized plugins providing dedicated, recommended lint rules for React components and DOM interactions.

**Gotchas**:
- The React Compiler is *not* enabled by default in this template due to potential impacts on development and build performance.
- For production use, developers must manually update ESLint configurations to enable type-aware lint rules for strict code quality assurance.
- When configuring type-aware linting, the `project` setting in `languageOptions` must point correctly to the relevant `tsconfig` files (`tsconfig.node.json` and `tsconfig.app.json`).