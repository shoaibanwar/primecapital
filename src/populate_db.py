import sqlite3
import config

def init_db():
    conn = sqlite3.connect(config.DATABASE_PATH)
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS financial_report (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        amount REAL NOT NULL
    )
    ''')

    # Insert initial data
    cursor.execute('INSERT INTO financial_report (name, amount) VALUES (?, ?)', ('Sample Report', 1000.0))
    cursor.execute('INSERT INTO financial_report (name, amount) VALUES (?, ?)', ('Test Report', 2000.0))
    cursor.executemany('''
    INSERT INTO financial_report (name, amount) VALUES (?, ?)
    ''', [('Revenue', 1000.0), ('Expenses', 500.0), ('Profit', 500.0)])

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
