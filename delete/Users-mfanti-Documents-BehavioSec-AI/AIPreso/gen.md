---
file_path: AIPreso/gen.py
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: py
---

**Purpose**: This script generates a detailed Microsoft PowerPoint presentation outlining various advanced Generative AI tools and demonstrating their practical use cases.

**What it does**:
- Initializes a new PowerPoint presentation using the `python-pptx` library.
- Defines a reusable internal helper function (`add_slide`) to consistently add content (title and bullet points) to new slides.
- Programmatically populates 10 slides with curated information covering topics such as Microsoft Copilot, Anthropic Claude, Google Gemini, and next-generation agentic development environments.
- Saves the completed presentation to a file named `Gen_AI_Tools_Presentation.pptx`.

**Key exports**:
- `create_presentation()`: The main function that orchestrates the entire process, from initialization to saving the final PowerPoint file.

**Gotchas**:
- **Hardcoded Layout Reliance**: The script assumes fixed placeholder indexes (`slide.placeholders[1]`) for titles and body content, making it sensitive to changes in the presentation template's layout structure.
- **Nested Functionality**: The core logic for content formatting is encapsulated in a local helper function (`add_slide`), which keeps the scope clean but limits the external reusability of that specific formatting logic.
- **Bullet Level Logic**: The `add_slide` function contains specific logic to determine bullet levels (`p.level = 1 if bullet.startswith("-") else 0`), which assumes consistency in the input list format.