from database import get_connection, init_db

init_db() 

conn = get_connection()

cursor = conn.execute(
    "INSERT INTO entries (user_id, mood_score, stress_score, journal_text) VALUES (?, ?, ?, ?)",
    (1, 35, 70, "Midterm tomorrow, stressed."),
)
entry_id = cursor.lastrowid

for name, color in [("school", "#5aaabb"), ("exams", "#be6040")]:
    conn.execute(
        "INSERT OR IGNORE INTO tags (user_id, name, color) VALUES (?, ?, ?)",
        (1, name, color),
    )
    tag_id = conn.execute(
        "SELECT tag_id FROM tags WHERE user_id = ? AND name = ?",
        (1, name),
    ).fetchone()["tag_id"]
    conn.execute(
        "INSERT INTO entry_tags (entry_id, tag_id) VALUES (?, ?)",
        (entry_id, tag_id),
    )

conn.commit()
conn.close()
print("Added a test entry")