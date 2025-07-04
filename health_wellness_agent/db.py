import sqlite3

def init_db():
    conn = sqlite3.connect('health_wellness.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            role TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_chat(email, role, message):
    conn = sqlite3.connect('health_wellness.db')
    c = conn.cursor()
    c.execute('INSERT INTO chat_history (email, role, message) VALUES (?, ?, ?)',
              (email, role, message))
    conn.commit()
    conn.close()

def get_chat(email):
    conn = sqlite3.connect('health_wellness.db')
    c = conn.cursor()
    c.execute('SELECT role, message FROM chat_history WHERE email = ?', (email,))
    data = c.fetchall()
    conn.close()
    return data
