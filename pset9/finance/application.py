import os
from tempfile import mkdtemp

from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   session)
from flask_session import Session
from werkzeug.exceptions import (HTTPException, InternalServerError,
                                 default_exceptions)
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import (apology, db, format_date, get_history, get_shares,
                     get_user, login_required, lookup, quote_buy, quote_sell,
                     reverse, usd, user_register, username_validator)

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd
app.jinja_env.filters["date"] = format_date
app.jinja_env.filters["reversed"] = reverse
app.jinja_env.filters["int"] = int

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session.get("user_id")
    user = get_user(user_id)
    shares = get_shares(user_id)
    total = sum([share["price"] for share in shares])

    return render_template("index.html", user=user, shares=shares, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")

    symbol = request.form.get("symbol")
    shares = int(request.form.get("shares"))
    
    if not symbol:
        return render_template("buy.html"), 400
    
    if shares < 1:
        return render_template("buy.html"), 400

    quote = lookup(symbol)

    if not quote:
        return render_template("buy.html"), 400

    if quote_buy(session.get("user_id"), symbol, shares, quote["price"]):
        return redirect("/")
    else:
        flash("Sorry! You don't have enough money!", "error")
        return render_template("buy.html"), 400


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return render_template("history.html", transactions=get_history(session.get("user_id")))


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure username was submitted
        if not username:
            flash("Must provide username!", "error")
            return render_template("login.html", password=password), 403

        # Ensure password was submitted
        elif not password:
            flash("Must provide password!", "error")
            return render_template("login.html", username=username), 403

        # Query database for username
        users = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username exists and password is correct
        if len(users) != 1 or not check_password_hash(users[0]["hash"], password):
            flash("Invalid username and/or password", "error")
            return render_template("login.html", username=username, password=password), 403

        # Remember which user has logged in
        session["user_id"] = users[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    
    symbol = request.form.get("symbol")
    
    if not symbol:
        flash("Sorry! I need a symbol to search a quote...", "warning")
        return render_template("quote.html"), 400

    response = lookup(symbol)

    if not response:
        flash("Sorry! I couldn't find a quote for this symbol...", "warning")
        return render_template("quote.html"), 400

    return render_template("quote.html", quote=response)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")
    
    if not username or not password or password != confirmation:
        flash("Username and Password are required, Password must be equal to Confirmation!")
        return render_template("register.html", username=username, password=password, confirmation=confirmation), 400

    registered = user_register(username=username, hash=generate_password_hash(password))

    if registered:
        flash('Registered!')
        return redirect("/")
    else:
        flash("User already exists!")
        return render_template("register.html", username=username, password=password, confirmation=confirmation), 400


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session.get("user_id")
    user_shares = get_shares(user_id)

    if request.method == "GET":
        return render_template("sell.html", shares=user_shares)

    quote = lookup(request.form.get("symbol"))
    shares = int(request.form.get("shares"))
    
    if shares < 1:
        return render_template("sell.html", shares=user_shares), 400

    if quote_sell(user_id, quote["symbol"], shares, quote["price"]):
        flash("Sold!")
        return redirect("/")
    else:
        flash("Sorry! You are trying to sell more than you have!...", "warning")
        return render_template("sell.html", shares=user_shares), 400


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)


@app.route("/user")
def user():
    return jsonify({"user": username_validator(request.args.get("username"))})
