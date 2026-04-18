---
file_path: demo-stitch/designlogistics.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document serves as a design blueprint for a simulated, client-side React SPA that showcases a comprehensive logistics and shipment management portal.

**What it does**:
- Simulates a full-featured user experience, including public marketing pages, secured dashboards, and detailed data display.
- Manages application state and routing using mock authentication via `localStorage`.
- Presents detailed, hardcoded demo data for shipment tracking, spending analytics, and SLA performance.
- Implements route guards to restrict access to the core shipment management dashboard.

**Key exports**:
- `useAuth.tsx`: Provides context-based authentication management, handling mock login, signup, and session persistence.
- `App.tsx`: Acts as the root component, configuring the `BrowserRouter` and implementing the primary route guard logic.
- `Dashboard.tsx`: Contains the main authenticated UI, displaying multiple tabs for shipments, history, and analytics using hardcoded demo data.
- `HomePage.tsx`: Renders the public-facing marketing site, outlining features and primary calls to action.

**Gotchas**:
- The application is entirely client-side; all data is hardcoded demo data and requires a backend API layer to be functional in a real-world scenario.
- Authentication is mocked (`useAuth.tsx`) and only uses `localStorage` for session persistence, acting as a thin shim for future Auth0 integration.
- The current implementation manages tab state locally (`useState`) within the Dashboard, meaning navigation between tabs is not synchronized with the URL (no deep linking).