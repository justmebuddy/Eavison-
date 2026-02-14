import sqlite3
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/securestack.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS scans(
id INTEGER PRIMARY KEY,
url TEXT,
risk TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS findings(
id INTEGER PRIMARY KEY,
url TEXT,
issue TEXT
)
""")

def save_scan(url, risk):
    cur.execute("INSERT INTO scans(url,risk) VALUES(?,?)",(url,risk))
    conn.commit()

def save_finding(url, issue):
    cur.execute("INSERT INTO findings(url,issue) VALUES(?,?)",(url,issue))
    conn.commit()