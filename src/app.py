"""Contains all routes of the Flask application."""

import secrets
import sqlite3

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    abort,
    session,
)

from users import create_user, check_login

app = Flask(__name__)
app.config["SECRET_KEY"] = "something"


def limit_length(string, maxlength):
    """Abort with 403 if string is empty or longer than maxlength."""
    if len(string) > maxlength or len(string) == 0:
        abort(403)


@app.route("/")
def index():
    """Render the front page."""
    return render_template("index.html", username=session.get("username"))


@app.route("/register")
def register():
    """Render the registration form."""
    return render_template("register.html")


@app.route("/create_account", methods=["POST"])
def create_account():
    """Handle new account creation and store user in database."""
    username = request.form["username"]
    limit_length(username, 30)

    password1 = request.form["password1"]
    limit_length(password1, 50)

    password2 = request.form["password2"]
    limit_length(password2, 50)

    if password1 != password2:
        flash("Error: Passwords did not match")
        return redirect("/register")

    try:
        create_user(username, password1)
        user_id = check_login(username, password1)

        session["user_id"] = user_id
        session["username"] = username
        session["csrf_token"] = secrets.token_hex(16)

        return redirect("/")
    except sqlite3.IntegrityError:
        flash("Username is occupied")
        return redirect("/register")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Render login page or authenticate user."""
    if request.method == "GET":
        return render_template("login.html")

    username = request.form["username"]
    password = request.form["password"]

    user_id = check_login(username, password)
    if user_id:
        session["user_id"] = user_id
        session["username"] = username
        session["csrf_token"] = secrets.token_hex(16)
        return redirect("/")

    flash("Error: Invalid username or password")
    return redirect("/login")


@app.route("/logout")
def logout():
    """Clear session and log out the user."""
    session.clear()
    return redirect("/")
