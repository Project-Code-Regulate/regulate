from contextlib import asynccontextmanager
from fastapi import Depends
from database import get_db
from fastapi import FastAPI
from datetime import datetime, timedelta, timezone
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


@app.get("/tags")
def get_tags(db=Depends(get_db)):
    rows = db.execute(
        """
        SELECT name, color
        FROM tags
        WHERE user_id = ?
        ORDER BY name
        """,
        (TEMP_USER_ID,),
    ).fetchall()
    return [dict(row) for row in rows]


@app.get("/charts/trends")
def get_chart_trends(
    start: datetime | None = None,
    end: datetime | None = None,
    tag: str | None = None,
    db=Depends(get_db),
):
    if end is None:
        end = datetime.now(timezone.utc)
    if start is None:
        start = end - timedelta(days=30)

    def to_db_time(t):
        if t.tzinfo is not None:
            t = t.astimezone(timezone.utc)
        return t.strftime("%Y-%m-%d %H:%M:%S")

    query = """
        SELECT entries.entry_id,
               strftime('%Y-%m-%dT%H:%M:%SZ', entries.created_at) AS created_at,
               entries.mood_score,
               entries.stress_score
        FROM entries
    """
    params = []

    if tag:
        query += """
        JOIN entry_tags ON entry_tags.entry_id = entries.entry_id
        JOIN tags ON tags.tag_id = entry_tags.tag_id AND tags.name = ?
        """
        params.append(tag)

    query += """
        WHERE entries.user_id = ?
          AND entries.created_at BETWEEN ? AND ?
        ORDER BY entries.created_at, entries.entry_id
    """
    params += [TEMP_USER_ID, to_db_time(start), to_db_time(end)]

    entries = []
    for row in db.execute(query, params).fetchall():
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
        entry["tags"] = [dict(t) for t in tag_rows]
        entries.append(entry)

    return entries