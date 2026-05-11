import sqlite3

conn = sqlite3.connect("jobfinder.db")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT,
    location TEXT,
    salary TEXT,
    experience TEXT,
    domain TEXT

)
''')

conn.commit()