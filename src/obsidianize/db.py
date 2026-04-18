import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Generator, Optional


@dataclass
class Project:
    id: int
    root_path: str
    vault_folder: str
    added_at: str
    last_sync_at: Optional[str]


@dataclass
class FileRecord:
    id: int
    project_id: int
    relative_path: str
    file_hash: str
    note_filename: str   # stem + .md, e.g. 'api.md'
    vault_subdir: str    # '' for root, subdir name otherwise
    status: str
    last_processed_at: str


class Database:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_schema()

    @contextmanager
    def _conn(self) -> Generator[sqlite3.Connection, None, None]:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    def _now(self) -> str:
        return datetime.now(timezone.utc).isoformat()

    def _init_schema(self) -> None:
        with self._conn() as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS projects (
                    id           INTEGER PRIMARY KEY AUTOINCREMENT,
                    root_path    TEXT UNIQUE NOT NULL,
                    vault_folder TEXT NOT NULL,
                    added_at     TEXT NOT NULL,
                    last_sync_at TEXT
                );

                CREATE TABLE IF NOT EXISTS files (
                    id                INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id        INTEGER NOT NULL,
                    relative_path     TEXT NOT NULL,
                    file_hash         TEXT NOT NULL,
                    note_filename     TEXT NOT NULL,
                    vault_subdir      TEXT NOT NULL DEFAULT '',
                    status            TEXT NOT NULL DEFAULT 'active',
                    last_processed_at TEXT NOT NULL,
                    FOREIGN KEY (project_id) REFERENCES projects(id),
                    UNIQUE (project_id, relative_path)
                );
            """)
            # Migration: add vault_subdir column to existing databases
            cols = [r[1] for r in conn.execute("PRAGMA table_info(files)").fetchall()]
            if "vault_subdir" not in cols:
                conn.execute(
                    "ALTER TABLE files ADD COLUMN vault_subdir TEXT NOT NULL DEFAULT ''"
                )

    # ── Projects ─────────────────────────────────────────────────────────────

    def get_project(self, root_path: str) -> Optional[Project]:
        with self._conn() as conn:
            row = conn.execute(
                "SELECT * FROM projects WHERE root_path = ?", (root_path,)
            ).fetchone()
            return Project(**dict(row)) if row else None

    def add_project(self, root_path: str, vault_folder: str) -> Project:
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO projects (root_path, vault_folder, added_at) VALUES (?, ?, ?)",
                (root_path, vault_folder, self._now()),
            )
        return self.get_project(root_path)  # type: ignore[return-value]

    def remove_project(self, root_path: str) -> None:
        project = self.get_project(root_path)
        if not project:
            return
        with self._conn() as conn:
            conn.execute("DELETE FROM files WHERE project_id = ?", (project.id,))
            conn.execute("DELETE FROM projects WHERE root_path = ?", (root_path,))

    def list_projects(self) -> list[Project]:
        with self._conn() as conn:
            rows = conn.execute("SELECT * FROM projects ORDER BY added_at").fetchall()
            return [Project(**dict(r)) for r in rows]

    def update_project_sync_time(self, project_id: int) -> None:
        with self._conn() as conn:
            conn.execute(
                "UPDATE projects SET last_sync_at = ? WHERE id = ?",
                (self._now(), project_id),
            )

    # ── Files ─────────────────────────────────────────────────────────────────

    def get_active_files(self, project_id: int) -> list[FileRecord]:
        with self._conn() as conn:
            rows = conn.execute(
                "SELECT * FROM files WHERE project_id = ? AND status = 'active'",
                (project_id,),
            ).fetchall()
            return [FileRecord(**dict(r)) for r in rows]

    def upsert_file(
        self,
        project_id: int,
        relative_path: str,
        file_hash: str,
        note_filename: str,
        vault_subdir: str,
        status: str,
    ) -> None:
        with self._conn() as conn:
            conn.execute(
                """
                INSERT INTO files
                    (project_id, relative_path, file_hash, note_filename, vault_subdir,
                     status, last_processed_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT (project_id, relative_path)
                DO UPDATE SET
                    file_hash         = excluded.file_hash,
                    note_filename     = excluded.note_filename,
                    vault_subdir      = excluded.vault_subdir,
                    status            = excluded.status,
                    last_processed_at = excluded.last_processed_at
                """,
                (project_id, relative_path, file_hash, note_filename, vault_subdir,
                 status, self._now()),
            )

    def mark_archived(self, project_id: int, relative_path: str) -> None:
        with self._conn() as conn:
            conn.execute(
                "UPDATE files SET status = 'archived' WHERE project_id = ? AND relative_path = ?",
                (project_id, relative_path),
            )
