from helpers import get_birthdays, add_birthday
import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


DAYS_OF_MONTHS = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database

        name = request.form.get("name")
        month = int(request.form.get("month"))
        day = int(request.form.get("day"))

        if not name:
            return redirect("/"), 400

        if not month or month > 12:
            return redirect("/"), 400

        if not day or day > DAYS_OF_MONTHS[month]:
            return redirect("/"), 400
        
        if add_birthday(name, month, day):
            return redirect("/")

        return redirect("/"), 400

    else:

        # TODO: Display the entries in the database on index.html

        birthdays = get_birthdays()

        return render_template("index.html", birthdays=birthdays)
