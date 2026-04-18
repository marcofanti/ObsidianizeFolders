---
file_path: demo-stitch/design.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This design document outlines the architecture and component structure for a client-side Single Page Application (SPA) simulating a personal finance dashboard using React, TypeScript, and hardcoded demo data.

**What it does**:
- Provides a complete, navigable UI skeleton for a finance dashboard, including dedicated pages for login, signup, and the main dashboard view.
- Manages client-side routing via React Router v6, implementing protected routes that guard access to the main dashboard view.
- Simulates user authentication flow using a mock context (`useAuth.tsx`) and persists the session state in `localStorage`.
- Displays a complex, multi-panel dashboard layout that utilizes pre-defined, hardcoded demo data for accounts, transactions, and insights.

**Key exports**:
- `App.tsx`: The root component responsible for setting up routing, the `AuthProvider` context, and implementing route guards.
- `useAuth.tsx`: Manages the mock authentication state, handling login, sign up, and session persistence via `localStorage`.
- `Dashboard.tsx`: The main protected view that orchestrates the layout, displaying accounts, transactions, and quick actions using static demo data.

**Gotchas**:
- The application has no actual backend; all data and state management are client-side and simulated (e.g., credentials validation, balance tracking).
- Authentication is mocked; the structure is explicitly prepared to swap in a real provider (e.g., Auth0).
- The design currently relies on a single global `index.css` file, avoiding modern CSS practices like CSS Modules or styled components.
- Tab state within the `Dashboard` component is managed locally via `useState` and is not synchronized with the URL, limiting deep linking capability to the dashboard sections.