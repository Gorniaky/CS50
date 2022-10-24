import os
from tempfile import mkdtemp

from flask import (Flask, flash, jsonify, redirect, render_template, request)
from flask_session import Session
from werkzeug.exceptions import (HTTPException, InternalServerError, default_exceptions)

from helpers import (apology, db, format_date, reverse, post_result, get_rankings)

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
app.jinja_env.filters["date"] = format_date
app.jinja_env.filters["reversed"] = reverse

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", rankings=get_rankings())

    return render_template("game.html", game_theme="number")


@app.route("/game", methods=["GET", "POST"])
def game():
    if request.method == "GET":
        return render_template("game.html")
    
    username = request.form.get("username")
    time = int(request.form.get("time"))
    points = int(request.form.get("points"))
    
    post_result(username=username, time=time, points=points)
    
    return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
