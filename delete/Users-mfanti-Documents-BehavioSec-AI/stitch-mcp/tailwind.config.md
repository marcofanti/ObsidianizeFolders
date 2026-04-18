---
file_path: stitch-mcp/banking/tailwind.config.js
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: js
---

**Purpose**: Configures the design tokens and utility classes for the Tailwind CSS framework, establishing a comprehensive design system palette and typography rules for the application.

**What it does**:
- Defines the content paths (`index.html`, `./src/**/*.{js,ts,jsx,tsx}`) that Tailwind CSS should scan for usage of utility classes.
- Enables dark mode using the `class` strategy, allowing CSS classes to toggle the theme.
- Extends the default theme with a highly detailed, multi-branded color palette (primary, secondary, tertiary, background, error) and specific typography definitions.

**Key exports**:
- **Color Palette**: Defines a vast set of semantic colors (e.g., `primary`, `secondary`, `tertiary`) along with corresponding text, background, and border variants (e.g., `primary-container`, `on-primary`).
- **Typography**: Sets specific font families for different components: `headline` (Newsreader/Georgia/serif), `body`/`label` (Manrope/sans-serif), and `mono` ("Roboto Mono"/monospace).
- **Spacing/Shape**: Overrides and extends border radius utilities with standardized sizes (e.g., `sm`, `lg`, `xl`, `full`).

**Gotchas**:
- The color system is highly prescriptive and uses multiple semantic groups (primary, secondary, tertiary) and intricate variants (e.g., `primary-fixed`, `on-secondary-container`), requiring developers to adhere strictly to these defined names.
- All custom color definitions must be prefixed by their group (e.g., `primary`, `secondary`) to ensure proper scoping within the utility classes.
- The `content` array dictates which files Tailwind will analyze; any components or styles added outside of `./index.html` or `./src/` will not be processed correctly unless the path is updated.