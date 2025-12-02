import sqlite3
from pathlib import Path

def get_connection():
    con = sqlite3.connect("database.db")
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con

def execute(sql, params=None):
    if params is None:
        params = []
    con = get_connection()
    try:
        cursor = con.execute(sql, params)
        con.commit()
        return cursor
    except sqlite3.OperationalError as e:
        print("SQLite OperationalError:", e)
        return None
    finally:
        con.close()

def query(sql, params=None):
    if params is None:
        params = []
    con = get_connection()
    result = con.execute(sql, params).fetchall()
    con.close()
    return result

def init_db():
    db_path = Path("database.db")
    if db_path.exists():
        return

    with sqlite3.connect(db_path) as con:
        con.execute("PRAGMA foreign_keys = ON")
        with open("src/database_files/schema.sql") as f:
            con.executescript(f.read())
