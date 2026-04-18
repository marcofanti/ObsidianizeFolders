---
file_path: demo-to-chris-empty/Test4.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: The file specifies the requirements for creating a complete, multi-page Single Page Application (SPA) structure using React/Vite, focusing on the UI scaffolding for authentication and dashboard views.

**What it does**:
- Creates a new SPA web application structure within a dedicated folder (`/gemini-test`).
- Implements necessary pages for user authentication (login, signup, password reset) and a main dashboard/landing page.
- Requires the application structure and CSS styling to mimic existing templates (`/templates2/Dashboard.tsx`, `/templates2/LoginPage.tsx`, `/templates2/SignupPage.tsx`).
- Uses React and Vite as the foundational technology stack.
- Excludes the actual backend login process, deferring authentication implementation to a future step (Auth0).

**Key exports**:
- N/A (The file outlines project requirements, not specific code exports.)

**Gotchas**:
- Must not implement the actual authentication logic; the provided login/signup pages must be UI stubs only.
- All existing content in the folder (other `.md` files, previous `/gemini-test-*`, or `/finance-app-*` folders) must be ignored or superseded.
- The `/templates` folder should be ignored and its styles/structure must be copied manually for the new project structure.
- The resulting application must be highly structured, requiring the developer to ask clarifying questions before commencing development.