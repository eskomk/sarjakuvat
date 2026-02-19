import db

def foreign_keys():
    sql = "PRAGMA foreign_keys = ON"
    db.query(sql)

def get_comics():
    sql = """SELECT c.id cid, c.title title, u.id uid, u.username username
        FROM comics c
        LEFT JOIN users u ON c.user_id = u.id
        GROUP BY c.id
        ORDER BY c.title ASC"""
    return db.query(sql)

def get_comics_paged(page, page_size):
    sql = """SELECT c.id cid, c.title title, u.id uid, u.username username
        FROM comics c
        LEFT JOIN users u ON c.user_id = u.id
        GROUP BY c.id
        ORDER BY c.title ASC
        LIMIT ? OFFSET ?"""

    limit = page_size
    offset = page_size * (page - 1)

    return db.query(sql, [limit, offset])


def get_plain_comics():
    sql = """SELECT c.id cid, c.title title, c.description desc, c.user_id adder_id
        FROM comics c"""
    return db.query(sql)

def get_comic(id: int):
    sql = """SELECT c.id cid, c.title title, c.description desc, c.user_id adder_id,
        u.username adder,
        ct.id ctid, ct.comic_type c_type
        FROM comics c
        LEFT JOIN users u ON c.user_id = u.id
        LEFT JOIN comic_types ct ON c.type_id = ct.id
        WHERE c.id = ?"""
    return db.query(sql, [id])[0]

def get_comic_star_for_user(user_id: int, comic_id: int):
    sql = """SELECT s.user_id user_id, s.comic_id comic_id,
        s.stars stars, s.description desc
        FROM comic_stars s
        WHERE s.user_id = ? AND s.comic_id = ?"""
    try:
        return db.query(sql, [user_id, comic_id])[0]
    except IndexError:
        return None

def get_stars_per_comic(comic_id: int):
    sql = """SELECT s.user_id user_id, s.comic_id comic_id,
        s.stars stars, s.description s_desc,
        c.title title, c.description c_desc
        FROM comics c
        JOIN comic_stars s ON c.id = s.comic_id
        WHERE s.comic_id = ?"""
    try:
        return db.query(sql, [comic_id])
    except IndexError:
        return None

def get_stars_per_comic_paged(comic_id: int, page, page_size):
    sql = """SELECT s.user_id user_id, s.comic_id comic_id,
        s.stars stars, s.description s_desc,
        c.title title, c.description c_desc
        FROM comics c
        JOIN comic_stars s ON c.id = s.comic_id
        WHERE s.comic_id = ?
        ORDER BY c.title
        LIMIT ? OFFSET ?"""

    limit = page_size
    offset = page_size * (page - 1)

    try:
        return db.query(sql, [comic_id, limit, offset])
    except IndexError:
        return None


def get_mean_stars_for_comic(comic_id: int):
    sql = """SELECT ROUND(AVG(stars), 2) as s_mean FROM comic_stars
        WHERE comic_id = ?"""
    try:
        return db.query(sql, [comic_id])[0]
    except IndexError:
        return None

def get_all_comic_types():
    sql = "SELECT id, comic_type FROM comic_types";
    return db.query(sql)

def get_comic_count():
    sql = "SELECT COUNT(*) cnt FROM comics"
    return db.query(sql)[0]

def get_user_count():
    sql = "SELECT COUNT(*) cnt FROM users"
    return db.query(sql)[0]

def get_comic_star_count(comic_id: int):
    sql = """SELECT COUNT(*) cnt FROM comic_stars
        WHERE comic_id = ?"""
    return db.query(sql, [comic_id])[0][0]

def get_comic_count_per_user(user_id: int):
    sql = "SELECT COUNT(*) cnt FROM comics WHERE user_id = ?"
    return db.query(sql, [user_id])[0]

