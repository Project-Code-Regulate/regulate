from contextlib import asynccontextmanager
from fastapi import Depends
from database import get_db
from fastapi import FastAPI

from database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

TEMP_USER_ID = 1

app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/journal")
def get_journal_entries(db=Depends(get_db)):
    entry_rows = db.execute(
        """
        SELECT entry_id, mood_score, stress_score, journal_text, created_at
        FROM entries
        WHERE user_id = ?
        ORDER BY created_at DESC, entry_id DESC
        """,
        (TEMP_USER_ID,),
    ).fetchall()

    entries = []
    for row in entry_rows:
        entry = dict(row)
        tag_rows = db.execute(
            """
            SELECT tags.name, tags.color
            FROM tags
            JOIN entry_tags ON entry_tags.tag_id = tags.tag_id
            WHERE entry_tags.entry_id = ?
            """,
            (row["entry_id"],),
        ).fetchall()
        entry["tags"] = [dict(tag) for tag in tag_rows]
        entries.append(entry)

    return entries