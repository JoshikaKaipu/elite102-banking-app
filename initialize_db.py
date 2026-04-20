import sqlite3

# This will create a file named 'bank.db' in your folder
DB_NAME = 'bank.db'

def initialize_database():
    # 1. Connect (this creates the file if it doesn't exist)
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    print("Creating banking tables...")

    # 2. Create the Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')

    # 3. Create the Accounts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            account_type TEXT,
            balance REAL DEFAULT 0.0,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')

    # 4. Insert a test user so the app isn't empty
    cursor.execute('''
        INSERT OR IGNORE INTO users (first_name, last_name, email) 
        VALUES ('John', 'Doe', 'john@example.com')
    ''')

    connection.commit()
    connection.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    initialize_database()
