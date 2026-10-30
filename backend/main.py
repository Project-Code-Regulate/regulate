from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from pydantic import BaseModel, Field

from database import get_db, init_db


TEMP_USER_ID = 1


class CheckInInput(BaseModel):
    mood: int = Field(ge=0, le=100)
    stress: int = Field(ge=0, le=100)
    text: str = ""
    tags: list[str] = Field(default_factory=list)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/checkin", status_code=201)
def submit_checkin(checkin: CheckInInput, db=Depends(get_db)):
    cursor = db.execute(
        """
        INSERT INTO entries (user_id, mood_score, stress_score, journal_text)
        VALUES (?, ?, ?, ?)
        """,
        (TEMP_USER_ID, checkin.mood, checkin.stress, checkin.text),
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
