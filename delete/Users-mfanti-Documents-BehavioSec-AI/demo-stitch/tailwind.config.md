---
file_path: demo-stitch/tailwind.config.ts
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: ts
---

**Purpose**: Configures Tailwind CSS utility classes, establishing a comprehensive, custom design system across colors, typography, and spacing for the application.

**What it does**:
- Specifies the content paths (`./index.html` and `./src/**/*.{ts,tsx}`) that Tailwind should scan for class usage.
- Activates dark mode using the `class` strategy, requiring specific classes to toggle the theme.
- Overrides and extends the default design system with custom design tokens (colors, font families, border radii).

**Key exports**:
- **Colors**: A detailed, multi-layered palette defining specific semantic roles (e.g., `primary`, `secondary`, `tertiary`), contrast states (`on-primary`, `on-secondary`), surface variations (`surface`, `surface-container`), and fixed/dim variations across multiple color families.
- **FontFamily**: Establishes a consistent typography scale using the 'Manrope' font family for headline, body, and label elements.
- **borderRadius**: Defines custom, limited scale options for corner rounding (e.g., `lg`, `xl`, `full`) while maintaining a small default value.

**Gotchas**:
- **Token Density**: The color configuration is highly detailed, utilizing numerous specific tokens (e.g., `on-secondary-fixed-variant`, `surface-container-low`) which implies a complex, predefined design system that developers must adhere to.
- **Dependencies**: The file implicitly relies on the 'Manrope' font being available and properly loaded in the project for the specified font families to function.
- **Content Scanning**: Changes to the file structure or content paths must be reflected in the `content` array to ensure Tailwind correctly generates styles for all components.