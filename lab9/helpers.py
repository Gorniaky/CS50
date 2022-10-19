from cs50 import SQL

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


def get_birthdays():
  return db.execute("SELECT * FROM birthdays")


def add_birthday(name: str, month: int, day: int):
  if db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, month, day):
    return True
  return False