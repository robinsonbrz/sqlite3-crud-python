import sqlite3
import sys

connection = sqlite3.connect("people.db")
cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE people (name, TEXT, age INTEGER, skills STRING)")
except Exception as e:
    pass

def user_is_unique(name):
    rows = cursor.execute("SELECT name, age, skills FROM people").fetchall()

    for user in rows:
        if user[0] == name:
            return False
    return True
