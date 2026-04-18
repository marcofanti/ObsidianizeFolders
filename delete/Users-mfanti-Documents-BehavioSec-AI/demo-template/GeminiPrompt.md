---
file_path: demo-template/GeminiPrompt.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: Defines the requirements and scope for building a boilerplate Single Page Application (SPA) for a modern financial dashboard using React/Vite.

**What it does**:
- Initializes a new project directory (`/gemini-test`).
- Structures the application to include boilerplate user authentication pages (login, signup, password reset) and error handling.
- Builds a main dashboard view featuring demo bank account data, styled similarly to an existing template.
- Mandates the use of specific existing template pages (e.g., `templates2/HomePage.tsx`) to copy structure and CSS styles.
- Explicitly ignores implementing real authentication logic, deferring that functionality to a later implementation phase (Auth0).

**Key exports**:
- **Project Structure**: A complete, working SPA scaffold initialized in `/gemini-test`.
- **Components**: Mocked structures for Login, Signup, Password Reset, and the main Dashboard/Bank Accounts view.

**Gotchas**:
- **Authentication State**: The actual backend authentication process must be mocked and is explicitly not to be implemented, as Auth0 will be added later.
- **Scope Limitation**: The generation process must ignore previous project directories (e.g., `/gemini-test-_` and `/finance-app-_`).
- **Read-Only Prompt**: The prompt itself specifies that it should not be updated.