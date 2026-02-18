import sqlite3

DB_PATH = "traffic.db"

def init_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        brand TEXT,
        confidence REAL,
        image_path TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Index to speed up brand queries
    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_brand 
    ON detections (brand);
    """)

    # Index to speed up time queries
    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_timestamp 
    ON detections (timestamp);
    """)

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_database()
