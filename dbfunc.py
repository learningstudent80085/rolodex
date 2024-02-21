import sqlite3

conn = sqlite3.connect("sample_db")

cursor = conn.cursor()

conn.close()