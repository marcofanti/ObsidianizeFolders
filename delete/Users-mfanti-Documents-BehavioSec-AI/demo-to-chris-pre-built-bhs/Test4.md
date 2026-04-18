---
file_path: demo-to-chris-pre-built-bhs/Test4.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: To scaffold a comprehensive Single Page Application (SPA) for a modern financial service using React and Vite, providing the necessary structure for user authentication and core dashboard views.

**What it does**:
- Creates a complete application shell including pages for user authentication, sign-up, password reset, and error handling.
- Establishes a clean project environment within a new `/gemini-test` directory.
- Develops a landing page and a post-login dashboard page that emulate the structure and CSS styles of existing templates (specifically `templates2/HomePage.tsx`).
- Implements the foundational UI/UX for login and sign-up using specified template copies.

**Key exports**:
- **Dashboard Page**: A modern financial dashboard showing sample bank accounts, adopting the structure and CSS of `templates2/HomePage.tsx`.
- **Login Page**: A structurally accurate imitation of the form and layout from `templates2/LoginPage.tsx`.
- **Signup Page**: A structurally accurate imitation of the form and layout from `templates2/SignupPage.tsx`.

**Gotchas**:
- The actual authentication process (login/sign-up validation) must be mocked or faked; real login logic (Auth0) is explicitly deferred.
- The project must strictly use a new folder (`/gemini-test`).
- The developer must ignore all previously existing content in the folder, including all other `.md` files, previous `gemini-test-` and `finance-app-` folders, and the entire `/templates` folder structure, utilizing only the specified template structures for adaptation.
- The required technology stack is React/Vite.