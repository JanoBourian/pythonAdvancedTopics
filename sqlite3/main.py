import sqlite3
import os

DATABASE_NAME = "tutorial.db"
directory = os.path.dirname(os.path.abspath(__file__))
database = os.path.join(directory, DATABASE_NAME)
con = sqlite3.connect(database)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS data(path, document, pwd, content)")
res = cur.execute("SELECT * FROM data")
print(res)
print(res.fetchone())