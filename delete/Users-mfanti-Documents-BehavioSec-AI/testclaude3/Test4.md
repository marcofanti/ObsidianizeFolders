---
file_path: testclaude3/Test4.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: To create a complete, modern single-page web application boilerplate using React/Vite for a financial service simulation, including mock implementations for all core authentication and display flows.

**What it does**:
- Scaffolds a new project folder (`/gemini-test`) using React and Vite.
- Sets up client-side routing (React Router DOM) for major application views (Landing, Dashboard, Login, Signup, Password Reset).
- Implements a mock authentication context (`useAuth.tsx`) using `localStorage` to manage user state.
- Copies and adapts the structure and CSS styles from provided template files to build the required pages.
- Provides a robust application structure including a custom `ProtectedRoute` wrapper and an explicit 404 error handling page.

**Key exports**:
- `gemini-test/src/App.tsx`: The core routing file containing protected routes and navigation logic.
- `gemini-test/src/useAuth.tsx`: A mock context providing state management for authentication (login/logout/signup).
- `gemini-test/src/LandingPage.tsx`: The primary landing page styled for a modern financial application.
- `gemini-test/src/Dashboard.tsx`: The main content page (demo bank accounts) structured similar to a professional dashboard view.
- `gemini-test/src/LoginPage.tsx`: The UI for user login, integrated into the routing structure.
- `gemini-test/src/SignupPage.tsx`: The UI for new user registration.
- `gemini-test/src/PasswordReset.tsx`: A dedicated page for managing password resets.
- `gemini-test/GeminiSkills.md`: A supplementary file listing the technical skills utilized during the development process.

**Gotchas**:
- The authentication process is fully mocked and does not connect to any real backend (Auth0/API integration is pending).
- The application relies on copying and adapting styling from specific template files, requiring the preservation of those CSS structures.
- The final structure includes extensive inline comments within `Test4.md` documenting every step taken, making the file highly informative but verbose.