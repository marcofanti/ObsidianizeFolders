---
file_path: demo-to-chris-pre-built/CLAUDEold.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: Provides comprehensive guidance and architectural details for developers utilizing the financial application demo built with React and TypeScript.

**What it does**:
- Manages user authentication and redirects between unauthenticated (landing page) and authenticated (dashboard) states using Auth0.
- Routes the application flow through a conditional rendering pattern based on the user's authentication status.
- Displays financial data, including bank accounts, recent transactions, and user profiles, utilizing hardcoded demo data structures.
- Supports both landing page presentation (marketing/login) and a complex dashboard interface (accounts, transactions).

**Key exports**:
- `useAuth0()`: The primary React hook used throughout the application to check authentication status (`isAuthenticated`, `isLoading`, `user`).
- `App.tsx`: The main routing component that determines whether to render the unauthenticated landing page or the authenticated dashboard.
- `Dashboard.tsx`: Contains the core logic and display for authenticated users, managing account, transaction, and profile views.
- `bankAccounts` / `recentTransactions`: Structured data constants defined within `Dashboard.tsx` that provide the mock financial information for the demo.

**Gotchas**:
- **Authentication Dependency**: The application logic heavily relies on the `useAuth0()` hook and must handle the three states (`loading`, `unauthenticated`, `authenticated`) using conditional rendering.
- **Data Modification**: To update the displayed financial data, developers must modify the constant arrays (`bankAccounts`, `recentTransactions`) directly at the top of `Dashboard.tsx`.
- **Styling Scope**: All global and component-specific styles are centralized in `index.css`, and developers should use BEM-like naming conventions for consistency.
- **Linting**: Type-aware linting is currently *not* enabled and requires an upgrade path documented elsewhere for full TypeScript safety.