---
file_path: demo-stitch/download_stitch.py
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: py
---

**Purpose**: This script downloads static assets (HTML and PNG images) for predefined screens of a user interface and saves them into a structured local directory.

**What it does**:
- Creates a directory structure `.stitch/designs` if it doesn't already exist.
- Iterates through a list of defined screens (e.g., "HomePage", "SignupPage").
- For each screen, it downloads the corresponding HTML content and PNG image from specified Google/Googleusercontent URLs.
- Saves the downloaded assets as `.html` and `.png` files, respectively, within the `.stitch/designs` directory, named after the screen.
- Uses a User-Agent header ('Mozilla/5.0') to ensure proper handling by the remote servers.

**Key exports**:
- Directory Structure: Creates the `.stitch/designs` directory to store all downloaded assets.
- Assets: Downloads and saves pairs of files: `[ScreenName].html` (the full screen content) and `[ScreenName].png` (a specific PNG asset/screenshot).

**Gotchas**:
- **Hardcoded URLs**: The screen definitions, including the complex `html_url` and `png_url` values, are hardcoded within the script and cannot be easily changed without modifying the source.
- **Network Dependencies**: The script relies on two external libraries (`urllib.request` and `os`) and requires the ability to reach the specified Googleusercontent URLs; download failures will be caught and printed to the console but will not halt the entire script.
- **Error Handling**: While basic `try...except` blocks are used to catch download failures, the script does not implement robust retry logic or sophisticated logging for failed downloads.