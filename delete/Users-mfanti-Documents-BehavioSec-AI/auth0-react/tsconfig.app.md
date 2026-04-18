---
file_path: auth0-react/tsconfig.app.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Configures the TypeScript compiler settings for a React application build, enforcing strict type checking and modern JavaScript standards compatible with bundlers like Vite.

**What it does**:
- Sets the compilation target to ES2023 and module system to ESNext, ensuring compatibility with modern JavaScript environments.
- Enforces extremely strict type checking across the entire codebase (`"strict": true`), catching unused variables and parameters.
- Configures the project for a bundler environment (`"moduleResolution": "bundler"`), allowing for modern import syntax while preventing the compiler from emitting output (`"noEmit": true`).
- Specifies React JSX handling using `"jsx": "react-jsx"`.

**Key exports**:
(This configuration file does not export code; it exports compiler settings.)

**Gotchas**:
- **No Output Generation**: Because `"noEmit": true` is set, this file assumes that a separate build tool (like Vite) is responsible for generating the final JavaScript output, and TypeScript is only used for type checking.
- **Strictness**: The configuration enforces very high levels of strictness (e.g., `noUncheckedSideEffectImports`, `verbatimModuleSyntax`), which might require developers to update existing codebases to pass all linting rules.
- **Local File Inclusion**: Only files within the `src` directory are included in this compilation configuration.