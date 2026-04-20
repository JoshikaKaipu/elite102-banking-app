import sqlite3
def createBank():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY,
            password TEXT,
            name TEXT,
            balance REAL
        )
    ''')
    conn.commit()
    conn.close()

def createAccount(newName, newPassword):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO accounts (name, password, balance) VALUES (?, ?, 0.00)", (newName, newPassword))

    conn.commit()
    conn.close()

    print(f"Account created for {newName}!")

def checkBalance(account_name):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE name = ?", (account_name,))
    row = cursor.fetchone()

    if row:
        print(f"Balance for {account_name}: ${row[0]}")
    else:
        print(f"Account for '{account_name}' not found.")

    
    conn.close()


def deposit(account_name, amount):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM accounts WHERE name = ?", (account_name,))
    account = cursor.fetchone()

    if account is None:
        print(f"Error: No account found for '{account_name}'. Please create an account first.")
        conn.close()
        return ""

    cursor.execute("""
        UPDATE accounts 
        SET balance = balance + ? 
        WHERE name = ?
    """, (amount, account_name))

    conn.commit()
    conn.close()

    print(f"Successfully deposited ${amount} for {account_name}.")
    checkBalance(account_name)


def withdraw(account_name, amount):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM accounts WHERE name = ?", (account_name,))
    account = cursor.fetchone()

    if account is None:
        print(f"Error: No account found for '{account_name}'. Please create an account first.")
        conn.close()
        return ""

    cursor.execute("""
        UPDATE accounts 
        SET balance = balance - ? 
        WHERE name = ?
    """, (amount, account_name))

    conn.commit()
    conn.close()

    print(f"Successfully deposited ${amount} for {account_name}.")
    checkBalance(account_name)

def login(account_name, password):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM accounts WHERE name = ? AND password = ?", (account_name, password))
    user = cursor.fetchone()
    
    conn.close()
    
    if user:
        return True
    else:
        return False


#createBank()

