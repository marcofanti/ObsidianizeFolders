---
file_path: demo-stitch/designretail.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document outlines the architecture, features, and design decisions for a client-side Single Page Application simulating a fully functional e-commerce storefront and customer account portal.

**What it does**:
- Simulates both the public shopping experience (HomePage) and the authenticated customer experience (Dashboard).
- Manages authentication state entirely client-side using React Context and `localStorage`.
- Implements complex routing with protected routes and redirects based on authentication status.
- Presents structured, hardcoded demo data to power key features like order history, spending insights, and loyalty status.

**Key exports**:
- `App.tsx`: Acts as the root component responsible for setting up the routing structure, applying authentication guards, and wrapping the application in the context provider.
- `useAuth.tsx`: Provides the global authentication context, handling mocked login, signup, and session persistence via `localStorage`.
- `HomePage.tsx`: Renders the public storefront, focusing on promoting featured products and showcasing e-commerce value propositions (shipping, returns, etc.).
- `Dashboard.tsx`: Renders the protected customer account portal, featuring tabs for orders, wishlists, and account insights.

**Gotchas**:
- The entire application is non-functional beyond the client side; all data (products, orders, user state) is mocked/hardcoded.
- The mock authentication system requires the explicit replacement of key logic points (e.g., `login`, `signup`) to integrate a real backend service like Auth0.
- Tab state management within the Dashboard (`Dashboard.tsx`) is local (`useState`) and does not support deep linking or URL-based routing.
- The application uses only plain CSS in `index.css`; no CSS module scoping or utility framework (like Tailwind) is implemented.