import sqlite3

def connect_to_database():
    conn = sqlite3.connect("DB/TokoSejahtera.db")
    conn.row_factory = sqlite3.Row
    return conn
