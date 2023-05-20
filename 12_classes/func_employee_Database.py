import sqlite3
import os


if os.path.exists("employee_fun.db"):
    os.remove("employee_fun.db")

con = sqlite3.connect("employee_fun.db")

cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, score)")

con.commit()

