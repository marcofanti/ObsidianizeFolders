---
file_path: stitch-mcp/design-retail.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file describes a single-page React application that simulates a comprehensive dashboard for managing retail store operations, including tracking inventory, orders, and sales performance.

**What it does**:
- Simulates a full store manager dashboard (dashboard, inventory, order management) using hardcoded demo data.
- Handles user authentication flow (mocking login, signup, and password reset).
- Provides a visual representation of core retail KPIs (Revenue, Orders, Items Sold) upon successful login.
- Renders structured components for managing product listings and order summaries.

**Key exports**:
- `DashboardPage.tsx`: The main authenticated view providing an overview of retail performance.
- `TopAppBar.tsx`: Handles persistent navigation and user profile management.
- `AuthContext.tsx`: Provides mock authentication state and login logic across the application.
- `mockData.ts`: Central repository for all static and demo data (products, orders, KPIs).
- `PrimaryButton.tsx`: A reusable, styled component for primary call-to-actions.

**Gotchas**:
- **No Backend:** The entire application uses hardcoded, client-side data (`mockData.ts`) and does not connect to a live database or API.
- **Mock Authentication:** The authentication flow is simulated (`AuthContext.tsx`) and is designed to be a thin shim for future integration (e.g., Auth0).
- **Local State:** The dashboard tab state is managed locally using `useState` within `DashboardPage` and is not linked to the URL path.