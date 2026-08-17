import sqlite3

conn = sqlite3.connect("zeechib.db")

#Return all table in the masterTable

print(conn.execute("SELECT name FROM sqlite_master WHERE type = 'table'").fetchall())

