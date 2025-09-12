import sqlite3


def setup():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
    """)
    cur.execute("INSERT INTO users (username, password) VALUES ('alice', 'secret')")
    cur.execute("INSERT INTO users (username, password) VALUES ('bob', 'hunter2')")
    conn.commit()
    print("Database initialized!")



def safe_login(username, password):
    cur.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )
    result = cur.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Login failed.")


def unsafe_login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Executing:", query)
    cur.execute(query)  # ❌ Dangerous
    result = cur.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Login failed.")


if __name__ == "__main__":
    print("=== Safe Login ===")
    safe_login("alice", "secret")

    print("\n=== Unsafe Login ===")
    unsafe_login("alice' --", "wrongpassword")

    print("\n=== Unsafe Login with SQL Injection ===")
    unsafe_login("alice' OR '1'='1", "anything")

    # WHERE A OR B AND C
    # A OR (B AND C)

    # WHERE username = 'alice' OR '1'='1' AND password = 'anything'
    # WHERE username = 'alice' OR ('1'='1' AND password = 'anything')
    # AND has higher precedence than OR
