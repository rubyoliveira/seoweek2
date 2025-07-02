import sqlite3
from datetime import datetime

DB_NAME = "smartsearch.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS searches (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              query TEXT NOT NULL,
              result_title TEXT NOT NULL,
              result_url TEXT NOT NULL,
              timestamp TEXT NOT NULL)
"""
    )
    conn.commit()
    conn.close()


def save_query_and_results(query, results):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    timestamp = datetime.now().isoformat()

    for title, url in results:
        c.execute(
            "INSERT INTO searches("
            "query, result_title, result_url, timestamp) VALUES ("
            "?, ?, ?, ?)",
            (query, title, url, timestamp),
        )
    conn.commit()
    conn.close()


def get_search_history(limit=10):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        """
        SELECT query, result_title, result_url, timestamp
        FROM searches
        ORDER BY timestamp DESC
        LIMIT ?""",
        (limit,),
    )

    rows = c.fetchall()
    conn.close()

    return [{"query": q, "title": t, "url": u, "timestamp": ts} for q, t, u, ts in rows]
