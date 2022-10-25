import webview
from flask import (Flask, redirect, render_template, request)
from werkzeug.exceptions import (HTTPException, InternalServerError, default_exceptions)

from helpers import (apology, format_date, reverse, post_result, get_rankings)

# Configure application
app = Flask(__name__)
window = webview.create_window("Memory Game", app, confirm_close=True, width=9999999, height=9999999)

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


webview.start(http_server=True, gui="edgehtml")