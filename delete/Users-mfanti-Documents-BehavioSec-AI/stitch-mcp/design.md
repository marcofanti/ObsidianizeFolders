---
file_path: stitch-mcp/design.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document serves as a design blueprint detailing the architecture, component structure, and mock implementation for a client-side single-page application simulating a personal finance dashboard.

**What it does**:
- Manages application flow using protected routes, redirecting unauthenticated users attempting to access the main dashboard.
- Provides a mock authentication system that persists user state and session information using `localStorage`.
- Renders a multi-tab layout that simulates viewing financial data (accounts, transactions, insights) using hardcoded demo data.

**Key exports**:
- `useAuth.tsx`: Provides the application's authentication context, handling mock login, signup, and session persistence.
- `App.tsx`: Sets up the global routing structure (`BrowserRouter`) and enforces authentication guards for protected routes.
- `Dashboard.tsx`: The core view that houses the simulated financial layout and displays all hardcoded demo account and transaction data.

**Gotchas**:
- All displayed financial data (accounts, transactions) is hardcoded demonstration data and is not backed by a live API or database.
- The authentication system is entirely mocked; persistence relies on `localStorage`, not a real session manager.
- The dashboard's tab state is managed using local component state (`useState`) and is not tied to the URL, meaning deep linking to specific tabs is not supported.
- The entire application uses a single global stylesheet (`index.css`) rather than component-scoped CSS modules.