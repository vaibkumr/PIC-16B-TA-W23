import sqlite3

DB_NAME = 'data/messages.db'

def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        username TEXT,
        message TEXT);"""
        c.execute(query)
        conn.commit()
    
def save_message(username, message):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO messages (username, message) VALUES (?, ?)", (username, message))
            conn.commit()

def fetch_messages(username):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM messages WHERE username = ?", (username,))
            rows = c.fetchall()
        messages = [{'username': row[1], 'message': row[2]} for row in rows]
        return messages 