import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
conn = sqlite3.connect(BASE_DIR / "ecom.db")

def get_answer_from_query(query: str) -> str:
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return str(rows)
    except Exception as e:
        return f"error: {str(e)}"
