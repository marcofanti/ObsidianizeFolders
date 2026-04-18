---
file_path: testclaude/securebank2/README.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file describes the setup and architecture for a standalone, full-stack financial demonstration application featuring session-based authentication.

**What it does**:
- Provides both a Java Spring Boot backend (API) and a React/TypeScript frontend.
- Handles user authentication (login/signup) using Spring Security and BCrypt hashing.
- Manages secure session state via `JSESSIONID` cookies.
- Serves API requests from the frontend proxy (Vite) to the backend, managing state via session cookies.
- Supports both local development (two terminals) and a manual production build process where the React build must be copied into the Spring Boot static resources.

**Key exports**:
- **`AuthController`**: Manages user authentication endpoints (`/api/auth/login`, `/api/auth/signup`, `/api/auth/me`).
- **`DashboardController`**: Serves core financial data endpoints (`/api/dashboard/accounts`, `/api/dashboard/transactions`).
- **`UserService`**: Implements the business logic for user management and acts as the `UserDetailsService`.
- **`useAuth.tsx`**: Provides the frontend context for managing authentication state and restoring the session on component mount.

**Gotchas**:
- **In-memory storage**: The `UserRepository` uses a `ConcurrentHashMap`, meaning all user data is lost upon application restart.
- **Manual Production Build**: The full application requires a non-standard deployment process: the React frontend must be built (`npm run build`), and the resulting `dist` contents must be manually copied into the Spring Boot backend's static resources directory.
- **Development Setup**: Development requires managing two separate running processes (backend on port 8080, frontend on port 5173) and relies on the Vite proxy to bridge the communication.
- **Authentication Mechanism**: Authentication is handled manually using Spring Security's programmatic methods, avoiding external identity providers like Auth0 or Okta.