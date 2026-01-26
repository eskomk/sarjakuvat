import db

def get_comics():
    sql = """SELECT c.id, c.title, COUNT(c.id) total
             FROM comics c
             GROUP BY c.id
             ORDER BY c.title ASC"""
    return db.query(sql)

def get_comic(id: int):
    sql = "select c.id, c.title as title, c.description from comics c where c.id = ?"
    return db.query(sql, [id])[0]
