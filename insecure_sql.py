import sqlite3
import sys


def find_user(db_path: str, username: str):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # VULNERABILITY: SQL injection via string concatenation
    query = f"SELECT id, username, email FROM users WHERE username = '{username}'"
    print("[DEBUG] Running query:", query)
    cur.execute(query)  # injection point

    rows = cur.fetchall()
    conn.close()
    return rows


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: insecure_sql.py <db_path> <username>")
        sys.exit(1)

    rows = find_user(sys.argv[1], sys.argv[2])
    for r in rows:
        print(rows)
