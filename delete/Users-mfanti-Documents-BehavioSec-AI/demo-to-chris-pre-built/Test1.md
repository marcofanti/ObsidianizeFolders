---
file_path: demo-to-chris-pre-built/Test1.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: Outlines the architectural plan and requirements for building a complete, modern financial application with built-in user authentication and a separate React frontend.

**What it does**:
- Creates a full user authentication flow including signup, login, and password verification.
- Establishes a financial dashboard landing page mimicking a modern bank account view.
- Utilizes an in-memory database for user data storage.
- Configures the backend using Java/SpringBoot with session-based Spring Security.
- Uses React/TypeScript as a separate Single Page Application (SPA) frontend served by Spring Boot.

**Key exports**:
- **Authentication**: Complete Spring Security implementation handling session cookies and user login/signup.
- **Frontend Structure**: React SPA components designed to interact with the Spring Boot backend for data and UI.
- **Dashboard/UI**: A simulated bank accounts dashboard page structure, adaptable from existing templates.

**Gotchas**:
- **Technology Stack**: The application must use Java/SpringBoot (Maven) on the backend and React/TypeScript for the frontend.
- **Authentication Flow**: Must strictly use session-based authentication via Spring Security cookies; external providers like Auth0 or Okta must be excluded.
- **Data Persistence**: User data handling is limited to an in-memory database for simplicity.
- **Integration**: The React frontend must be served as static files by the Spring Boot backend.
- **Initial Setup**: Specific demo users (`mfanti@behaviosec.com`, password `0cramItnaf!`) must be pre-loaded into the database.