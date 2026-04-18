---
file_path: demo-to-chris-pre-built/GeminiSkills.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document catalogs the specific AI and development skills utilized during the construction and refinement of the Financial Single Page Application (SPA).

**What it does**:
- Analyzes and clarifies project requirements by referencing existing documentation and constraints.
- Rapidly scaffolds a modern React/TypeScript environment using tools like Vite.
- Manages complex application state (e.g., authentication) using custom React Context and local persistence.
- Adapts large, pre-existing UI components and replaces live API calls with static mock data.
- Structures application security using dedicated protected and public routing components.
- Validates code integrity and catches regressions through disciplined build pipelines and TypeScript typing.

**Gotchas**:
- The application utilizes modern React patterns, specifically relying on `useContext` and closures to manage complex state and simulate asynchronous API network delays.
- Frontend development was modularized by implementing dedicated `<ProtectedRoute>` boundaries to ensure effective, isolated state verification based on authentication status.
- Successful data migration required cleanly replacing all external API fetches with controlled, local mock state variables (`DEMO_ACCOUNTS`, `DEMO_TRANSACTIONS`).