---
file_path: demo-to-chris-pre-built/Skills.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: To document the complete technical stack, development methodologies, and architectural patterns employed during the development of the FinanceApp.

**What it does**:
- Details the specific tools and techniques utilized during development (e.g., using `Glob` for file discovery and `Read (parallel)` to minimize I/O round-trips).
- Maps the entire technology stack, identifying the primary role for each library and framework.
- Summarizes complex architectural patterns implemented within the application (e.g., protected routes and state management solutions).

**Key exports**:
- **React**: Core library responsible for UI component rendering.
- **TypeScript**: Provides strong type checking and type safety throughout the codebase.
- **React Router DOM**: Manages the application's client-side routing and navigation structure.
- **React Context + localStorage**: The established pattern for implementing mock authentication state management.

**Gotchas**:
- The development process required upfront clarification by asking the user critical questions (app name, mock auth behavior) before any code was written.
- Backend dependency was successfully avoided by utilizing hardcoded/mock data in the Dashboard and using local storage for state management.
- The implementation utilized `TodoWrite` to track progress across multiple distinct, sequential implementation steps.