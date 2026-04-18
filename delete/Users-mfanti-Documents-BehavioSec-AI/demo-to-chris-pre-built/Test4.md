---
file_path: demo-to-chris-pre-built/Test4.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: To establish the scaffolding for a complete, modern Single Page Application (SPA) designed for a financial service, including all necessary user authentication flows.

**What it does**:
- Initializes a new project using the `react/vite` stack within a designated `/gemini-test` folder.
- Creates and structures core user pages: Landing Page, Login, Signup, Password Reset, and dedicated error handling.
- Styles the application to resemble a modern financial institution interface, drawing structure and CSS from existing templates (`templates2/HomePage.tsx`, `templates2/Dashboard.tsx`, etc.).
- Provides a functional placeholder (demo) dashboard that simulates bank account views.

**Key exports**:
- **Dashboard**: The main view displayed post-login, simulating a financial account summary.
- **Login/Signup/Password Reset**: Core, functional pages handling the visual structure of user authentication processes.
- **Error Handling**: Dedicated page/mechanism to display application errors.

**Gotchas**:
- **Authentication is Mocked**: The actual login processing is *not* implemented and must be updated later using Auth0.
- **Environment Restriction**: The setup must ignore all previous test folders (`/gemini-test-*`, `/finance-app-*`) and ignore the entire `/templates` directory.
- **Styling Dependency**: The structure and CSS styling for the landing and key pages must be copied directly from specified `templates2` files.