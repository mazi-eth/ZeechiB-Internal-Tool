import sqlite3

#Read schema into db
conn = sqlite3.connect("zeechib.db")
conn.executescript(open("schema.sql").read())

tables = conn.execute("SELECT name FROM sqlite_master WHERE type = 'table'").fetchall()

print("Tables created: ", tables)

conn.close()
