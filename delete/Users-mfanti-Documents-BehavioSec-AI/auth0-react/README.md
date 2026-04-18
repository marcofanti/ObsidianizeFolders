---
file_path: auth0-react/README.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This template provides a minimal, functional setup for developing a React application using TypeScript, Vite, and includes detailed guidance on advanced ESLint configuration for production use.

**What it does**:
- Sets up a basic React environment using Vite and TypeScript, supporting HMR and basic ESLint rules.
- Provides instructions on using different Vite plugins (`@vitejs/plugin-react` or `@vitejs/plugin-react-swc`) depending on the desired underlying compiler (Oxc or SWC).
- Guides developers on upgrading the ESLint configuration to utilize type-aware lint rules for production applications.
- Demonstrates how to integrate specialized React-specific lint rules using `eslint-plugin-react-x` and `eslint-plugin-react-dom`.

**Key exports**:
- `tseslint.configs.recommendedTypeChecked`: Recommended configuration for enabling type-aware linting in TypeScript/TSX files.
- `tseslint.configs.strictTypeChecked`: Alternative configuration for enabling stricter, type-aware linting.
- `reactX.configs['recommended-typescript']`: ESLint configuration recommended for enforcing React-specific rules.
- `reactDom.configs.recommended`: ESLint configuration recommended for enforcing rules related to React DOM usage.

**Gotchas**:
- The React Compiler is intentionally not enabled on the template due to potential negative impacts on development and build performance.
- For production applications, developers must manually update the ESLint configuration to use type-aware lint rules (`recommendedTypeChecked` or `strictTypeChecked`).
- When extending ESLint, developers must update their `languageOptions` to correctly specify `project` and `tsconfigRootDir` paths for type checking to work.