---
file_path: stitch-mcp/logisticsdemo/MEMORY.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file documents the technical architecture, routing map, setup requirements, and key development lessons for the `logisticsdemo` React application component of the stitch-mcp project.

**What it does**:
- Defines the project environment using the Vite + React + TypeScript + Tailwind CSS stack.
- Maps all application routes, indicating component usage and required authentication status (e.g., `/dashboard` requires login).
- Provides mock authentication credentials for development testing.
- Outlines the project structure, including where static data, hooks, and UI components reside.

**Key exports**:
- `src/data/mockData.ts`: Central location for all static application data and corresponding TypeScript types.
- `src/hooks/`: Contains reusable logic hooks for managing form state and submission flows (e.g., `useLoginForm`).
- `src/components/ui/`: Houses reusable, atomic UI components like `FormInput`, `PrimaryButton`, and `ShipmentCard`.

**Gotchas**:
- **Vite/TypeScript Syntax**: Due to Vite 8's module enforcement, TypeScript `interface` and type-only imports MUST be explicitly imported using `import type { ... }` to prevent runtime `SyntaxError`s.
- **Google Fonts Loading**: For reliable operation with PostCSS, load external Google Fonts via a standard `<link>` tag in `index.html` rather than using the CSS `@import` rule.