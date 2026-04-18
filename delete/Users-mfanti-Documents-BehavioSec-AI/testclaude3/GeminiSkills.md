---
file_path: testclaude3/GeminiSkills.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: Documents the comprehensive suite of AI capabilities and engineering skills used to scaffold, develop, and verify a multi-file full-stack web application.

**What it does**:
- Analyzes multiple source files (`.tsx`, `.md`) simultaneously to build a cohesive architectural plan.
- Initializes the full development environment using standard tooling (e.g., `npx create-vite` for React/TypeScript).
- Creates complex, structured front-end features, including protected routes and simulated state management (`AuthContext`).
- Validates code quality and type safety through build process simulation (`npm run build`).
- Maintains transparent project tracking by generating and updating status logs (`task.md`).

**Key exports**:
- React Component Library: Scalable, functional components structured for a modern SPA.
- Project Architecture: A fully initialized, routed web application template (Vite/React/TS).
- Authentication Context: Simulated user authentication state utilizing `localStorage` for persistent session management.

**Gotchas**:
- The process heavily relies on analyzing disparate files (multi-file context) to ensure the final implementation adheres strictly to all perceived user constraints.
- The project structure utilizes advanced modern web standards (NextJS/Vite, `react-router-dom`) requiring deep knowledge of frontend tooling lifecycle.
- State management for features like authentication is implemented using simulation (`AuthContext` and `localStorage`), rather than a backend service, limiting persistence to the client side.