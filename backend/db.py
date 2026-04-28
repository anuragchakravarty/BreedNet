import sqlite3
from datetime import datetime

DB_NAME = "breednet.db"

# ------------------ CONNECTION ------------------
def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

# ------------------ CREATE TABLE ------------------
def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            animal TEXT NOT NULL,
            breed TEXT NOT NULL,
            confidence REAL NOT NULL,
            scanned_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

# ------------------ INSERT SCAN ------------------
def insert_scan(animal: str, breed: str, confidence: float):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO scans (animal, breed, confidence, scanned_at)
        VALUES (?, ?, ?, ?)
    """, (
        animal,
        breed,
        confidence,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()

# ------------------ FETCH HISTORY ------------------
def get_all_scans():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT animal, breed, confidence, scanned_at
        FROM scans
        ORDER BY id DESC
    """)

    rows = cur.fetchall()
    conn.close()

    return [
        {
            "animal": r[0],
            "breed": r[1],
            "confidence": r[2],
            "time": r[3]
        }
        for r in rows
    ]

# ------------------ CLEAR HISTORY ------------------
def clear_scans():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM scans")
    conn.commit()
    conn.close()