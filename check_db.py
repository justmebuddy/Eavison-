import sqlite3

conn = sqlite3.connect("data/securestack.db")
cur = conn.cursor()

print("=== SCANS TABLE ===")
for row in cur.execute("SELECT * FROM scans"):
    print(row)

print("\n=== FINDINGS TABLE ===")
for row in cur.execute("SELECT * FROM findings"):
    print(row)