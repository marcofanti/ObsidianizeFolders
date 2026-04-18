---
file_path: testclaude3/Thinking.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: To plan and implement a full-stack, session-based web banking application featuring secure user authentication and dashboard data viewing.

**What it does**:
- Manages the entire application lifecycle, serving a React SPA frontend built with TypeScript and Vite.
- Provides secure user authentication via custom REST API endpoints (`/api/auth/*`), utilizing Spring Security session cookies.
- Simulates core banking functionality by exposing endpoints for fetching user accounts and transaction history.
- Structures the final deployment to package both the Spring Boot backend and the compiled React frontend assets into a single runnable JAR.

**Key exports**:
- **`/api/auth/login` (POST)**: Validates user credentials, establishes a secure session cookie, and returns user details.
- **`/api/auth/signup` (POST)**: Registers a new user and handles initial password hashing.
- **`/api/auth/me` (GET)**: Retrieves the currently authenticated user's profile information based on the session cookie.
- **`/api/accounts` (GET)**: Returns sample bank account data.
- **`/api/transactions` (GET)**: Returns sample transaction history data.
- **`AuthContext`**: A custom React context that manages global user state (logged in/out) and handles the entire authentication flow across the SPA.

**Gotchas**:
- **Development vs. Production Deployment**: The system uses a development workflow where the Vite server proxies API calls to the Spring Boot backend (avoiding CORS issues), but the production build requires the React assets to be copied directly into Spring Boot's static resources directory.
- **Session Management**: Authentication relies heavily on session cookies. The plan requires careful configuration of Spring Security to manage the `SecurityContext` and must consider CORS headers and `SameSite` cookie attributes for reliable cross-origin communication.
- **Security Best Practice**: Passwords are never stored in plain text; they must be hashed using BCrypt during user registration and stored in the in-memory repository.
- **SPA Fallback**: The Spring Boot backend must implement a fallback routing mechanism (a dedicated controller) to ensure all client-side routed paths return `index.html`, allowing React Router to take over client-side navigation.