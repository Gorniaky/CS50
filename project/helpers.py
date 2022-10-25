import datetime
import os
from typing import Any

from cs50 import SQL
from flask import render_template

# Configure CS50 Library to use SQLite database
homepath = os.path.expanduser("~") + "/.memory"
if not os.path.exists(homepath):
    os.makedirs(homepath)
if not os.path.exists(homepath + "/memory.db"):
    open(homepath + "/memory.db", "w").close()
db = SQL("sqlite:///" + homepath + "/memory.db")


SQL_COMMANDS = [
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT)",
    "CREATE TABLE IF NOT EXISTS rankings (id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER,points INTEGER,time INTEGER)",
]
for command in SQL_COMMANDS:
    if command:
        print(command)
        print(db.execute(command))


""" for command in sqlCommands:
    if command:
        print(db.execute(command)) """


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
            ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")
        ]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def format_date(value):
    return datetime.datetime.fromtimestamp(int(value))


def reverse(value: list[Any]):
    value.reverse()
    return value


def post_result(username: str, points: int, time: int):
    user_id = db.execute("INSERT INTO users (username) VALUES (?)", username)
    db.execute("INSERT INTO rankings (user_id, points, time) VALUES (?, ?, ?)",
               user_id, points, time)


def get_rankings():
    return db.execute(
        "SELECT * " +
        "FROM users " +
        "JOIN rankings " +
        "ON users.id = rankings.user_id " +
        "ORDER BY points DESC, time, username "
    )