import db

def get_comics():
    sql = """SELECT c.id cid, c.title title, u.id uid, u.username username
             FROM comics c
             LEFT JOIN users u ON c.user_id = u.id
             GROUP BY c.id
             ORDER BY c.title ASC"""
    return db.query(sql)

def get_comic(id: int):
    sql = """SELECT c.id cid, c.title title, c.description desc, c.user_id adder_id,
        u.username adder
        FROM comics c
        LEFT JOIN users u ON c.user_id = u.id
        WHERE c.id = ?"""
    return db.query(sql, [id])[0]
