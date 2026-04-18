---
file_path: demo-to-chris-pre-built-bhs/Test1.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: Implement a standalone, full-stack user authentication system for a simulated modern financial application using Java Spring Boot and a React SPA frontend.

**What it does**:
- Establishes the complete user authentication lifecycle, including login, signup, password verification, and error handling.
- Initializes the application with a pre-populated set of demo users using an in-memory database.
- Serves the React frontend (SPA) statically via the Spring Boot backend.
- Handles user sessions and security using Spring Security session cookies.
- Replicates the structure and style of a modern dashboard upon successful login.

**Key exports**:
- Authentication Flow: Defines the robust mechanisms for user registration and secure login.
- Application Structure: Provides the architectural blueprint for separating the backend API (Spring Boot) from the modern frontend UI (React).

**Gotchas**:
- The application must be entirely standalone, requiring the removal of all dependencies or references to external identity providers (Auth0 or Okta).
- Data persistence is scoped to an in-memory database for simplicity, meaning user data will not survive application restarts.
- The entire implementation process, including all steps taken, must be documented in a `Claude.md` file.