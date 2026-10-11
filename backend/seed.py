import json
from main import get_connection

with get_connection() as conn:
    conn.execute(
        "INSERT INTO journal_entries (mood, stress, text, tags) VALUES (?, ?, ?, ?)",
        (65, 70, "Midterm tomorrow, stressed.", json.dumps(["school", "exams"])),
    )
    conn.execute(
        "INSERT INTO journal_entries (mood, stress, text, tags) VALUES (?, ?, ?, ?)",
        (15, 25, "Dinner with friends, felt relaxed.", json.dumps(["friends"])),
    )

conn.commit()
conn.close()
print("Seeded!")