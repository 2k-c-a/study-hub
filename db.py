import sqlite3
from contextlib import contextmanager
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "study_hub.db"
SCHEMA_PATH = BASE_DIR / "schema.sql"


@contextmanager
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        with conn:
            yield conn
    finally:
        conn.close()


def init_db():
    with get_conn() as conn:
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))


def list_studies():
    with get_conn() as conn:
        rows = conn.execute("SELECT * FROM studies ORDER BY id").fetchall()
    return [dict(row) for row in rows]


def create_study(title, description="", place="", max_members=4):
    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO studies (title, description, place, max_members) VALUES (?, ?, ?, ?)",
            (title, description, place, max_members),
        )
        return cur.lastrowid


def delete_study(study_id):
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM studies WHERE id = ?", (study_id,))
        return cur.rowcount > 0
