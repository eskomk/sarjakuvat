import sqlite3
from flask import Flask
from flask import redirect, render_template, request, flash
from flask import session
from flask import abort
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import db
import forum, users, config
import secrets
import math

app = Flask(__name__)
app.secret_key = config.secret_key

@app.context_processor
def inject_csrf_token():
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(16)
    return dict(csrf_token=session["csrf_token"])

@app.before_request
def csrf_protect():
    if request.method == "POST" and request.endpoint not in ("login",):
        session_token = session.get("csrf_token")
        form_token = request.form.get("csrf_token")
        if not session_token or session_token != form_token:
            abort(403)

@app.route("/")
@app.route("/<int:page>")
def index(page=1):
    forum.foreign_keys()

    page_size = 10
    comic_count = forum.get_comic_count()
    page_count = math.ceil(comic_count[0] / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect("/1")
    if page > page_count:
        return redirect("/" + str(page_count))

    comics = forum.get_comics_paged(page, page_size)
    return render_template("index.html", page=page, page_count=page_count, comics=comics)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create_user", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]

    if (not username or len(username) > 12) \
        or (not password1 or len(password1) > 12):
        flash("VIRHE: tunnus tai salasana epäkelvot (esim. > 12 merkkiä)")
        return redirect("/")

    password2 = request.form["password2"]
    if password1 != password2:
        flash("VIRHE: salasanat eivät ole samat")
        return redirect("/")
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

@app.route("/comic_issue/<int:comic_id>")
@app.route("/comic_issue/<int:comic_id>/<int:page>")
def show_comic(comic_id, page=1):
    username = ""

    try:
        username = session["username"]
    except KeyError:
        flash("VIRHE: Et ole kirjautunut sisään")
        return redirect("/login")

    comic_a = forum.get_comic(comic_id)
    # stars_per_comic_a = forum.get_stars_per_comic_paged(comic_id)
    mean_stars_a = forum.get_mean_stars_for_comic(comic_id)

    page_size = 10
    comic_star_count = forum.get_comic_star_count(comic_id)
    page_count = math.ceil(comic_star_count / page_size)
    page_count = max(page_count, 1)

    stars_per_comic_a = forum.get_stars_per_comic_paged(comic_id, page, page_size)

    if page < 1:
        # return redirect("/1")
        return redirect(f"/comic_issue/{comic_id}/1")

    if page > page_count:
        # return redirect("/" + str(page_count))
        return redirect(f"/comic_issue/{comic_id}/{str(page_count)}")

    return render_template("comic.html", comic=comic_a, starrings=stars_per_comic_a, \
        username=username, user_id=session["user_id"], mean_stars = mean_stars_a, \
        page=page, page_count=page_count)

@app.route("/add_comic", methods=["GET", "POST"])
def create_comic():
    comic_types_a = forum.get_all_comic_types()

    if request.method == "GET":
        return render_template("new_comic.html", c_types=comic_types_a)

    if request.method == "POST":
        title = request.form["title"]
        descr = request.form["description"]
        comic_type = request.form["type_value"]

        if (not title or len(title) > 100) or (not descr or len(descr) > 500) \
            or (not comic_type):
            flash("VIRHE: Epätäydelliset tiedot")
            return render_template("new_comic.html", c_types=comic_types_a)

        user_id = session["user_id"]
        sql = "INSERT INTO comics (title, description, user_id, type_id) VALUES (?, ?, ?, ?)"

        try:
            db.execute(sql, [title, descr, user_id, comic_type])
        except sqlite3.IntegrityError:
            flash("VIRHE: Titteli on jo varattu")
            # return redirect("/add_comic")
            return render_template("new_comic.html", c_types=comic_types_a)

        flash(f"Sarjis '{title}' luotu")
        return redirect("/")

@app.route("/user/<int:user_id>")
@app.route("/user/<int:user_id>/<int:page>")
def show_user(user_id, page=1):
    if page < 1:
        page = 1

    page_size = 10
    limit = page_size
    offset = page_size * (page - 1)

    comic_count = forum.get_comic_count_per_user(user_id)
    page_count = math.ceil(comic_count[0] / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect("/user/" + str(user_id) + "/1")
    if page > page_count:
        return redirect("/user/" + str(user_id) + "/" + str(page_count))

    # comiclist = forum.get_comics_per_user(user_id, limit, offset)

    user = users.get_user(user_id, limit, offset)

    return render_template("user.html", user = user, page=page, page_count = page_count)

@app.route("/userlist")
def list_users():
    userlist = users.get_users2()
    comics_plain_a = forum.get_plain_comics()
    return render_template("users.html", userlist = userlist, comics_plain = comics_plain_a)

@app.route("/userlist_paged")
@app.route("/userlist_paged/<int:page>")
def list_users_paged(page=1):
    if page < 1:
        page = 1

    page_size = 1
    limit = page_size
    offset = page_size * (page - 1)

    user_count = forum.get_user_count()
    page_count = math.ceil(user_count[0] / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect("/userlist_paged/1")
    if page > page_count:
        return redirect("/userlist_paged/" + str(page_count))

    userlist = users.get_users2_paged(limit, offset)
    comics_plain_a = forum.get_plain_comics()
    return render_template("users.html", userlist = userlist, comics_plain = comics_plain_a, page=page, page_count=page_count)

@app.route("/true_userlist_paged")
@app.route("/true_userlist_paged/<int:page>")
def true_userlist_paged(page=1):
    if page < 1:
        page = 1

    page_size = 10
    limit = page_size
    offset = page_size * (page - 1)

    user_count = forum.get_user_count()
    page_count = math.ceil(user_count[0] / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect("/true_userlist_paged/1")
    if page > page_count:
        return redirect("/true_userlist_paged/" + str(page_count))

    userlist = users.get_users2_paged(limit, offset)
    return render_template("users_wo_comics.html", userlist = userlist, page=page, page_count = page_count)


@app.route("/edit_comic/<int:comic_id>", methods=["GET", "POST"])
def edit_comic(comic_id):
    comic_a = forum.get_comic(comic_id)
    comic_types_a = forum.get_all_comic_types()

    if session["user_id"] != comic_a["adder_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("edit_comic.html", comic=comic_a, c_types=comic_types_a)

    if request.method == "POST":
        title = request.form["title"]
        descr = request.form["description"]
        comic_type = request.form["type_value"]

        if (not title or len(title) > 100) or (not descr or len(descr) > 500) \
            or (not comic_type):
            flash("VIRHE: Epätäydelliset tiedot")
            return render_template("edit_comic.html", comic=comic_a, c_types=comic_types_a)

        # user_id = session["user_id"]
        sql = "UPDATE comics SET title = ?, description = ?, type_id = ? WHERE id = ?"

        try:
            db.execute(sql, [title, descr, comic_type, comic_id])
        except sqlite3.IntegrityError:
            flash("VIRHE: Titteli on jo varattu tai muu virhe")
            # return redirect("/add_comic")
            return render_template("edit_comic.html", comic=comic_a, c_types=comic_types_a)

        flash(f"Sarjista '{title}' muokattu")
        return redirect("/")

@app.route("/delete_comic/<int:comic_id>", methods=["GET", "POST"])
def delete_comic(comic_id):
    comic_a = forum.get_comic(comic_id)

    if session["user_id"] != comic_a["adder_id"]:
        abort(403)

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

@app.route("/find_comics")
def find():
    sql = """SELECT id, title, description desc, user_id FROM comics
        WHERE title LIKE ? OR description LIKE ?"""

    query = request.args.get("query")

    if query:
        like = "%" + query + "%"
        results = db.query(sql, [like, like])
    else:
        query = ""
        results = []
    return render_template("find_comics.html", query = query, results = results)

@app.route("/star_comic/<int:comic_id>", methods=["GET", "POST"])
def star_comic(comic_id: int):
    comic_a = forum.get_comic(comic_id)

    if session["user_id"] == comic_a["adder_id"]:
        # abort(403)
        flash("VIRHE! Et voi arvostella omaa sarjistasi")
        return redirect("/")

    user_id = session["user_id"]
    stars_a = forum.get_comic_star_for_user(user_id, comic_id)

    if request.method == "GET":
        return render_template("star_comic.html", comic = comic_a, starring = stars_a)

    if request.method == "POST":
        stars = request.form["star_value"]
        if not stars or int(stars) < 1 or int(stars) > 5:
            flash("VIRHE: tähdet pielessä")
            return render_template("star_comic.html", comic = comic_a, starring = stars_a)
        descr = request.form["description"]
        if len(descr) > 500:
            flash("VIRHE: liian pitkä kuvaus")
            return render_template("star_comic.html", comic = comic_a, starring = stars_a)
        # user_id = session["user_id"]

        sql = "INSERT INTO comic_stars (stars, description, user_id, comic_id) VALUES (?, ?, ?, ?)"
        str_db_oper = "luotu"

        if stars_a:
            sql = """UPDATE comic_stars SET stars  = ?, description = ?
                WHERE user_id = ? AND comic_id = ?"""
            str_db_oper = "päivitetty"

        try:
            db.execute(sql, [stars, descr, user_id, comic_id])
        except sqlite3.IntegrityError:
            flash("VIRHE: Arvostelu ei onnannu, tietokantavirhe")
            return redirect("/")

        flash(f"Arvostelu {str_db_oper}. Sarjis: \"{comic_a['title']}\"")
        return redirect(f"/comic_issue/{comic_id}")
