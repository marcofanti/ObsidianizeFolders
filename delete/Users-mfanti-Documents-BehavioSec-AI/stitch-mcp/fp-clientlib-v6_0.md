---
file_path: stitch-mcp/ln/fp-clientlib-v6_0.js
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: js
---

**Purpose**: This file initializes and manages the functionality of the ThreatMetrix Fingerprint (FP) Client Library, handling resource loading, event tracking, and profile data capture on the client side.

**What it does**:
- Initializes sophisticated client-side event listeners (using techniques like `addEventListener` and proxy objects) to track user interactions and environment details.
- Manages the loading of external tracking scripts and resources within hidden iframes (`tmx_tags_iframe_...`) for privacy and isolation.
- Provides methods to control the timing and method of data loading (`WAIT_FOR_ONLOAD`, `RUN_IMMEDIATE`, etc.).
- Captures device and browser information (User Agent, OS, browser specifics) to build a behavioral fingerprint.
- Allows manual triggering of the profiling mechanism (`threatmetrix.profile`) using defined parameters (e.g., session ID, data).

**Key exports**:
- `threatmetrix.load_method.WAIT_FOR_ONLOAD`: Executes data loading logic only after the entire page has finished loading (`onload`).
- `threatmetrix.load_method.RUN_IMMEDIATE`: Executes data loading logic as soon as possible, regardless of page load state.
- `threatmetrix.load_method.RUN_IMMEDIATE_IFRAME`: Executes data loading logic using an iframe, providing strong resource isolation.
- `threatmetrix.profile(a, b, c, d, f, e)`: The primary function used to manually start the fingerprinting process, accepting various data parameters (e.g., user agent, session ID) and controlling the execution method.

**Gotchas**:
- **Obfuscation/Minification**: The code is heavily minified, making variable names and flow control difficult to follow without context.
- **Environment Dependence**: The library uses numerous browser-specific checks (`navigator.userAgentData`, `window.localStorage`, checking for `addEventListener` vs `attachEvent`) to ensure cross-browser compatibility.
- **Asynchronous Execution**: Data loading is highly asynchronous, often relying on `setTimeout` and `onload` events to manage resource dependencies and prevent race conditions during fingerprinting.
- **Scope Pollution**: The file directly attaches methods to the global scope using the `r` function (e.g., `r("threatmetrix.load_method.WAIT_FOR_ONLOAD", 0)`), creating global dependencies.