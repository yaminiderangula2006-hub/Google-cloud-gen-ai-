import sqlite3

DB_NAME = "emotion.db"


def initialize_database():

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        text TEXT,

        emotion TEXT,

        confidence REAL,

        response TEXT,

        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()

    conn.close()


def insert_record(text, emotion, confidence, response):

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO history
        (
            text,
            emotion,
            confidence,
            response
        )
        VALUES
        (?,?,?,?)
        """,
        (
            text,
            emotion,
            confidence,
            response
        )
    )

    conn.commit()

    conn.close()


def fetch_history():

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM history ORDER BY created DESC"
    )

    data = cur.fetchall()

    conn.close()

    return data