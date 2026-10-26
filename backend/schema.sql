-- foreign keys only work if PRAGMA foreign_keys = ON (done in database.py)

CREATE TABLE IF NOT EXISTS users (
    user_id     INTEGER PRIMARY KEY,
    username    TEXT    NOT NULL UNIQUE,
    email       TEXT    UNIQUE,
    created_at  TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- mood: 0 = very unpleasant, 100 = very pleasant
-- stress: 0 = low, 100 = high
CREATE TABLE IF NOT EXISTS entries (
    entry_id      INTEGER PRIMARY KEY,
    user_id       INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    mood_score    INTEGER NOT NULL CHECK (mood_score BETWEEN 0 AND 100),
    stress_score  INTEGER NOT NULL CHECK (stress_score BETWEEN 0 AND 100),
    journal_text  TEXT,
    created_at    TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_entries_user_created ON entries(user_id, created_at);

CREATE TABLE IF NOT EXISTS tags (
    tag_id   INTEGER PRIMARY KEY,
    user_id  INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    name     TEXT    NOT NULL COLLATE NOCASE,
    color    TEXT    NOT NULL DEFAULT '#ccaa6a'
             CHECK (color GLOB '#[0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f]'),
    UNIQUE (user_id, name)
);

CREATE TABLE IF NOT EXISTS entry_tags (
    entry_id  INTEGER NOT NULL REFERENCES entries(entry_id) ON DELETE CASCADE,
    tag_id    INTEGER NOT NULL REFERENCES tags(tag_id) ON DELETE CASCADE,
    PRIMARY KEY (entry_id, tag_id)
);

CREATE INDEX IF NOT EXISTS idx_entry_tags_tag ON entry_tags(tag_id);