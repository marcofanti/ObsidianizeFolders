---
file_path: stitch-mcp/Tasks.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file defines a comprehensive, multi-stage industrial replication workflow that generates a complete application prototype, moving from an initial industry concept through design generation, external project setup, and final conversion into a structured React component library.

**What it does**:
- Prompts the user to define a target industry, enforcing strict naming conventions for all subsequent files and variables.
- Generates a specialized design brief and corresponding multiple screens (e.g., LandingPage, DashboardPage) by adapting a template to the specified industry.
- Initializes an external development project (Stitch) using the generated design assets.
- Converts the visual design assets into a modular, scalable React component system, defining all necessary routes, context, and architectural files.

**Key exports**:
- **React Component System**: A structured application front-end comprising typed components organized by routes (e.g., `/dashboard`) and separated into dedicated folders for UI, layout, and hooks.
- **Mock Authentication**: Defines static user credentials (`demo@{industryname}app.com`, etc.) and the dedicated `AuthContext.tsx` for managing state.
- **Design Assets**: The final, industry-specific set of UI screens and the corresponding `design-{industryname}.md` brief, ensuring visual consistency across the platform.

**Gotchas**:
- **Naming Convention Rigidity**: Industry names must be strictly managed: use short abbreviations (no hyphens) for variables/files (e.g., `health`), but use hyphenated names for folder structures and URLs (e.g., `health-app`).
- **TypeScript Imports**: When using Vite 8 with `verbatimModuleSyntax`, all type-only values (`interface`, model definitions) must be imported using `import type { ... }` to prevent runtime `SyntaxError`s.
- **Google Fonts Implementation**: Fonts must be loaded via `<link>` tags in `index.html` rather than using `@import` in CSS to successfully bypass PostCSS resolution failures.