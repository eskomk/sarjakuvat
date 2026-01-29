import sqlite3
from flask import Flask
from flask import redirect, render_template, request, flash
from flask import session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import db
import forum, users, config

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    comics = forum.get_comics()
    return render_template("index.html", comics = comics)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create_user", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
        last_id = db.last_insert_id()

        if last_id:
            session["user_id"] = last_id
            session["username"] = username
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    flash("Tunnus luotu")
    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            flash("VIRHE: väärä tunnus tai salasana")
            return redirect("/login")


@app.route("/logout")
def logout():
    del session["user_id"]
    del session["username"]
    return redirect("/")

@app.route("/comic_juttu/<int:comic_id>")
def show_comic(comic_id):
    comic_a = forum.get_comic(comic_id)

    try:
        username = session["username"]
    except KeyError:
        flash("VIRHE: Et ole kirjautunut sisään")
        return redirect("/login")
    return render_template("comic.html", comic=comic_a, username=username, user_id = session["user_id"])

@app.route("/add_comic", methods=["GET", "POST"])
def create_comic():
    if request.method == "GET":
        return render_template("new_comic.html")

    if request.method == "POST":
        title = request.form["title"]
        descr = request.form["description"]
        user_id = session["user_id"]
        sql = "INSERT INTO comics (title, description, user_id) VALUES (?, ?, ?)"

        try:
            db.execute(sql, [title, descr, user_id])
        except sqlite3.IntegrityError:
            flash("VIRHE: Titteli on jo varattu")
            # return redirect("/add_comic")
            return render_template("new_comic.html")

        flash("Titteli luotu")
        return redirect("/")

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)

    return render_template("user.html", user = user)

@app.route("/edit_comic/<int:comic_id>", methods=["GET", "POST"])
def edit_comic(comic_id):
    comic_a = forum.get_comic(comic_id)

    if request.method == "GET":
        return render_template("edit_comic.html", comic = comic_a)

    if request.method == "POST":
        title = request.form["title"]
        descr = request.form["description"]
        # user_id = session["user_id"]
        sql = "UPDATE comics SET title = ?, description = ? WHERE id = ?"

        try:
            db.execute(sql, [title, descr, comic_id])
        except sqlite3.IntegrityError:
            flash("VIRHE: Titteli on jo varattu")
            # return redirect("/add_comic")
            return render_template("edit_comic.html")

        flash(f"Sarjista '{title}' muokattu")
        return redirect("/")

@app.route("/delete_comic/<int:comic_id>", methods=["GET", "POST"])
def delete_comic(comic_id):
    comic_a = forum.get_comic(comic_id)

    if request.method == "GET":
        return render_template("delete_comic.html", comic = comic_a)

    if request.method == "POST":
        sql = "DELETE FROM comics WHERE id = ?"

        try:
            db.execute(sql, [comic_id])
        except sqlite3.IntegrityError:
            flash("VIRHE: Sarjista ei voitu poistaa")
            return render_template("edit_comic.html")

        flash(f"Sarjis \'{comic_a['title']}\' poistettu")
        return redirect("/")

