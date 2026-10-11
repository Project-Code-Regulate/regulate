import json
import sqlite3
from fastapi import FastAPI

app = FastAPI()

DB_PATH = "regulate.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

with get_connection() as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS journal_entries (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            mood       INTEGER NOT NULL,
            stress     INTEGER NOT NULL,
            text       TEXT NOT NULL DEFAULT '',
            tags       TEXT NOT NULL DEFAULT '[]'
        )
    """)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/journal")
def get_journal_entries():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM journal_entries ORDER BY created_at DESC"
        ).fetchall()
    entries = []
    for row in rows:
        entry = dict(row)
        entry["tags"] = json.loads(entry["tags"])
        entries.append(entry)
    return entries