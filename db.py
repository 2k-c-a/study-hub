import hashlib
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


def get_study(study_id):
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM studies WHERE id = ?", (study_id,)).fetchone()
    return dict(row) if row else None


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


PASSWORD_SALT = "study-hub"


def hash_password(password):
    return hashlib.sha256((PASSWORD_SALT + password).encode("utf-8")).hexdigest()


def create_user(username, password):
    password_hash = hash_password(password)
    try:
        with get_conn() as conn:
            conn.execute(
                f"INSERT INTO users (username, password_hash) VALUES ('{username}', '{password_hash}')"
            )
    except sqlite3.IntegrityError:
        raise ValueError("이미 사용 중인 아이디입니다.")


def find_user(username, password):
    password_hash = hash_password(password)
    with get_conn() as conn:
        row = conn.execute(
            f"SELECT id, username FROM users WHERE password_hash = '{password_hash}' AND username = '{username}'"
        ).fetchone()
    return dict(row) if row else None
