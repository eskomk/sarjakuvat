from werkzeug.security import check_password_hash
import db

def check_login(username, password):
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    result = db.query(sql, [username])

    if len(result) == 1:
        user_id, password_hash = result[0]
        if check_password_hash(password_hash, password):
            return user_id

    return None

def get_user(user_id):
    sql = """SELECT u.id uid, u.username uname, c.id cid, c.title title, c.description desc
             FROM users u
             LEFT JOIN comics c ON u.id = c.user_id
             WHERE u.id = ?"""
    result = db.query(sql, [user_id])
    return result if result else None

def get_users():
    sql = """SELECT u.id uid, u.username uname, c.id cid, c.title titteli, c.description desc
             FROM users u
             LEFT JOIN comics c ON u.id = c.user_id"""
    result = db.query(sql)
    return result if result else None

def get_users2():
    sql = "SELECT u.id uid, u.username uname FROM users u"
    result = db.query(sql)
    return result if result else None

def get_users2_paged(limit, offset):
    sql = "SELECT u.id uid, u.username uname FROM users u ORDER BY uname LIMIT ? OFFSET ?"

    result = db.query(sql, [limit, offset])
    return result if result else None
