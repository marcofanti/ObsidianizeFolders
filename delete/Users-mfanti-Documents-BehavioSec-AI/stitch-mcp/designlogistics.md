---
file_path: stitch-mcp/designlogistics.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document outlines the architecture and design specifications for a client-side, single-page application (SPA) simulating a comprehensive logistics and shipment management portal.

**What it does**:
- Simulates the full user journey, including public marketing views (Homepage) and protected, data-intensive shipment management operations (Dashboard).
- Provides mock authentication, persisting session status and user data in `localStorage`.
- Renders complex, multi-tabbed interfaces (Dashboard) and detailed feature showcases (Homepage) using hardcoded demo data.
- Manages navigation using React Router v6, enforcing route guards to protect the main dashboard area.

**Key exports**:
- `useAuth.tsx`: Manages mock user session context, handling login, signup, and logout, with state persistence in `localStorage`.
- `App.tsx`: Serves as the root component, implementing high-level route protection and wrapping the application with the Auth context.
- `HomePage.tsx`: The public marketing landing page, designed to capture leads by showcasing core logistics features (Tracking, Customs, Coverage).
- `Dashboard.tsx`: The protected, authenticated portal where users manage shipments, view history, and track performance metrics.

**Gotchas**:
- The entire application operates with no backend connectivity; all data displayed (shipments, spending, ETAs) is hardcoded demo data (`DEMO_SHIPMENTS`).
- Authentication is a thin, mock layer designed for developer use, making session management client-side via `localStorage`.
- The dashboard's tab state (`activeTab`) is managed via local component state (`useState`) and is not linked to the URL, which prevents deep linking into specific internal tabs.
- The architecture is explicitly designed to be "Auth0-ready," meaning the current mock authentication logic must be replaced at three specific points to integrate a real provider.