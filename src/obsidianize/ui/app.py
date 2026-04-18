from pathlib import Path

import streamlit as st
from dotenv import dotenv_values, set_key

from obsidianize.config import DEFAULT_PROMPT, load_config
from obsidianize.db import Database
from obsidianize.notes import vault_folder_name
from obsidianize.sync import sync_project

_ENV_FILE = Path(".env")

_PROVIDERS = ["gemini", "ollama", "openai"]


def _env() -> dict[str, str]:
    return dict(dotenv_values(_ENV_FILE)) if _ENV_FILE.exists() else {}


def _save(key: str, value: str) -> None:
    set_key(str(_ENV_FILE), key, value)


# ── Page setup ──────────────────────────────────────────────────────────────

st.set_page_config(page_title="Obsidianize", page_icon="📝", layout="wide")
st.title("📝 Obsidianize")

tab_dashboard, tab_settings = st.tabs(["Dashboard", "Settings"])

# ── Settings tab ────────────────────────────────────────────────────────────

with tab_settings:
    st.header("Settings")
    env = _env()

    with st.form("settings_form"):
        vault_path = st.text_input(
            "Obsidian Vault Path", value=env.get("OBSIDIAN_VAULT_PATH", "")
        )

        col1, col2 = st.columns(2)
        with col1:
            provider_idx = _PROVIDERS.index(env.get("LLM_PROVIDER", "gemini"))
            provider = st.selectbox("LLM Provider", _PROVIDERS, index=provider_idx)
            model = st.text_input("LLM Model", value=env.get("LLM_MODEL", "gemini-2.0-flash"))
            api_key = st.text_input(
                "API Key", value=env.get("LLM_API_KEY", ""), type="password"
            )
        with col2:
            ollama_url = st.text_input(
                "Ollama Base URL",
                value=env.get("OLLAMA_BASE_URL", "http://localhost:11434"),
            )
            ollama_model = st.text_input(
                "Ollama Model", value=env.get("OLLAMA_MODEL", "llama3.2")
            )

        include_ext = st.text_input(
            "Include Extensions (comma-separated)",
            value=env.get("INCLUDE_EXTENSIONS", ".py,.js,.ts,.md,.txt,.yaml,.toml,.json,.sh"),
        )
        exclude_dirs = st.text_input(
            "Exclude Directories (comma-separated)",
            value=env.get("EXCLUDE_DIRS", "node_modules,.git,__pycache__,.venv,dist,build"),
        )
        max_index = st.number_input(
            "Max Index Entries (0 = unlimited)",
            value=int(env.get("MAX_INDEX_ENTRIES", "50")),
            min_value=0,
        )
        prompt_template = st.text_area(
            "Summary Prompt Template",
            value=env.get("SUMMARY_PROMPT_TEMPLATE", "") or DEFAULT_PROMPT,
            height=300,
        )

        if st.form_submit_button("Save Settings"):
            for key, val in [
                ("OBSIDIAN_VAULT_PATH", vault_path),
                ("LLM_PROVIDER", str(provider)),
                ("LLM_MODEL", model),
                ("LLM_API_KEY", api_key),
                ("OLLAMA_BASE_URL", ollama_url),
                ("OLLAMA_MODEL", ollama_model),
                ("INCLUDE_EXTENSIONS", include_ext),
                ("EXCLUDE_DIRS", exclude_dirs),
                ("MAX_INDEX_ENTRIES", str(int(max_index))),
                ("SUMMARY_PROMPT_TEMPLATE", prompt_template),
            ]:
                _save(key, val)
            st.success("Settings saved. Reload the page to apply.")

# ── Dashboard tab ────────────────────────────────────────────────────────────

with tab_dashboard:
    st.header("Projects")

    try:
        config = load_config()
    except ValueError as exc:
        st.error(str(exc))
        st.info("Configure your vault path in the **Settings** tab.")
        st.stop()

    db = Database(config.vault_path / "obsidianize.db")

    # Add project
    with st.expander("➕ Add Project"):
        new_path = st.text_input("Project Path", key="new_project_path")
        if st.button("Add & Sync") and new_path:
            root = Path(new_path).resolve()
            if not root.exists():
                st.error(f"Path does not exist: {root}")
            else:
                folder = vault_folder_name(root)
                if not db.get_project(str(root)):
                    db.add_project(str(root), folder)
                with st.spinner(f"Syncing {root}…"):
                    result = sync_project(root, db, config)
                st.success(
                    f"+{len(result.added)} added  "
                    f"~{len(result.updated)} updated  "
                    f"-{len(result.archived)} archived"
                )
                if result.failed:
                    st.warning(f"{len(result.failed)} file(s) failed — check logs.")
                st.rerun()

    # Project list
    projects = db.list_projects()
    if not projects:
        st.info("No projects registered. Add one above.")
    else:
        for project in projects:
            files = db.get_active_files(project.id)
            last_sync = project.last_sync_at[:10] if project.last_sync_at else "never"

            with st.container(border=True):
                col_path, col_folder, col_files, col_sync = st.columns([3, 2, 1, 1])
                col_path.markdown(f"**{project.root_path}**")
                col_folder.caption(project.vault_folder)
                col_files.metric("Files", len(files))
                col_sync.caption(f"Last sync: {last_sync}")

                btn_col, _ = st.columns([1, 5])
                if btn_col.button("Sync now", key=f"sync_{project.id}"):
                    with st.spinner(f"Syncing {project.root_path}…"):
                        result = sync_project(Path(project.root_path), db, config)
                    st.success(
                        f"+{len(result.added)} added  "
                        f"~{len(result.updated)} updated  "
                        f"-{len(result.archived)} archived  "
                        f"{result.unchanged} unchanged"
                    )
                    if result.failed:
                        st.warning(f"{len(result.failed)} file(s) failed.")
                    st.rerun()
