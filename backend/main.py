from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from pydantic import BaseModel, Field

from database import get_db, init_db


TEMP_USER_ID = 1


class CheckInInput(BaseModel):
    mood_score: int = Field(ge=0, le=100)
    stress_score: int = Field(ge=0, le=100)
    journal_text: str = ""
    tags: list[str] = Field(default_factory=list)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


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


@app.post("/checkin", status_code=201)
def submit_checkin(checkin: CheckInInput, db=Depends(get_db)):
    cursor = db.execute(
        """
        INSERT INTO entries (user_id, mood_score, stress_score, journal_text)
        VALUES (?, ?, ?, ?)
        """,
        (
            TEMP_USER_ID,
            checkin.mood_score,
            checkin.stress_score,
            checkin.journal_text,
        ),
    )
    entry_id = cursor.lastrowid

    for tag_name in checkin.tags:
        tag_name = tag_name.strip()
        if not tag_name:
            continue

        db.execute(
            "INSERT OR IGNORE INTO tags (user_id, name) VALUES (?, ?)",
            (TEMP_USER_ID, tag_name),
        )
        tag = db.execute(
            "SELECT tag_id FROM tags WHERE user_id = ? AND name = ?",
            (TEMP_USER_ID, tag_name),
        ).fetchone()

        db.execute(
            "INSERT OR IGNORE INTO entry_tags (entry_id, tag_id) VALUES (?, ?)",
            (entry_id, tag["tag_id"]),
        )

    db.commit()
    return {"entry_id": entry_id, "status": "created"}