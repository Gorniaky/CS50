import datetime
import os
from typing import Any
import urllib.parse
from functools import wraps

import requests
from cs50 import SQL
from flask import redirect, render_template, session
from finance import sqlCommands

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


for command in sqlCommands:
    if command:
        print(db.execute(command))


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


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()

        if not len(db.execute("SELECT * FROM companies WHERE symbol = ?", quote["symbol"])):
            db.execute("INSERT INTO companies (symbol, name) VALUES (?, ?)",
                       quote["symbol"], quote["companyName"])

        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


def user_register(username: str, hash: str):
    if username_validator(username):
        return False
    user_id = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
    if user_id:
        session["user_id"] = user_id
        return True
    else:
        return False


def username_validator(username: str):
    if len(db.execute("SELECT * FROM users WHERE username = ?", username)):
        return True
    return False


def get_user(id: str):
    return db.execute("SELECT username, cash FROM users WHERE id = ?", id)[0]


def quote_buy(user_id: int, symbol: str, shares: int, price: float):
    total = float(shares) * price

    user = db.execute("SELECT * FROM users WHERE id = ? AND cash >= ?", user_id, total)

    if not len(user):
        return False

    db.execute("INSERT INTO transactions (user_id, symbol, shares, price, transacted) VALUES (?, ?, ?, ?, ?)",
               user_id, symbol, shares, price, datetime.datetime.now().timestamp())

    user_shares = db.execute(
        "SELECT * FROM user_shares WHERE user_id = ? AND symbol = ?", user_id, symbol)

    if len(user_shares):
        db.execute("UPDATE user_shares SET shares = shares + ?, price = price + ? WHERE user_id = ? AND symbol = ?",
                   shares, total, user_id, symbol)
    else:
        db.execute("INSERT INTO user_shares (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   user_id, symbol, shares, total)

    db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total, user_id)

    return True


def quote_sell(user_id: int, symbol: str, shares: int, price: float):
    total = float(shares) * price

    user_shares = db.execute(
        "SELECT * FROM user_shares WHERE user_id = ? AND symbol = ? AND shares >= ?", user_id, symbol, shares)

    if not len(user_shares):
        return False

    db.execute("INSERT INTO transactions (user_id, symbol, shares, price, transacted) VALUES (?, ?, ?, ?, ?)",
               user_id, symbol, -shares, price, int(datetime.datetime.now().timestamp()))

    db.execute("UPDATE user_shares SET shares = shares - ?, price = price - ? WHERE user_id = ? AND symbol = ?",
               shares, total, user_id, symbol)

    db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total, user_id)

    return True


def get_shares(user_id: int):
    return db.execute(
        "SELECT * FROM user_shares JOIN companies ON user_shares.symbol == companies.symbol WHERE user_id = ? AND shares > 0", user_id
    )


def get_history(user_id: int):
    return db.execute("SELECT * FROM transactions JOIN companies ON transactions.symbol == companies.symbol WHERE user_id = ?", user_id)


def format_date(value):
    return datetime.datetime.fromtimestamp(int(value))


def reverse(value: list[Any]):
    value.reverse()
    return value
