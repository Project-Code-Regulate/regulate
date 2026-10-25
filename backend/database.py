import sqlite3
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent
DB_PATH = BACKEND_DIR / "regulate.db"
SCHEMA_PATH = BACKEND_DIR / "schema.sql"


def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_connection()
    try:
        conn.executescript(SCHEMA_PATH.read_text())
        # default user until we have login
        conn.execute(
            "INSERT OR IGNORE INTO users (user_id, username) VALUES (1, 'default')"
        )
        conn.commit()
    finally:
        conn.close()


def get_db():
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()