import random
import sqlite3
from werkzeug.security import generate_password_hash

db = sqlite3.connect("database.db")

db.execute("DELETE FROM comic_stars")
db.execute("DELETE FROM comics")
db.execute("DELETE FROM users")

user_count = 1000
comic_count = 10**5
star_count = 10**6

print("Aloitan ...")

for i in range(1, user_count + 1):
    db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
               ["user" + str(i), generate_password_hash("password" + str(i))])

print("Users done")

for i in range(1, comic_count + 1):
    c_user_id = random.randint(1, user_count)
    c_type_id = random.randint(1, 5)
    db.execute("INSERT INTO comics (title, description, user_id, type_id) VALUES (?, ?, ?, ?)",
               ["comic_title" + str(i), "descr" + str(i), c_user_id, c_type_id])

print("Comics done")

star_key_lista = []
for i in range(1, star_count + 1):
    while True:
        user_id = random.randint(1, user_count)
        comic_id = random.randint(1, comic_count)
        # star_key_lista.append((user_id, comic_id))
        if (user_id, comic_id,) not in star_key_lista:
            star_key_lista.append((user_id, comic_id,))
            break

    if i % 20000 == 0:
        print(f"stars {i}")

    stars_num = random.randint(1, 5)
    db.execute("""INSERT INTO comic_stars (stars, description, user_id, comic_id)
                  VALUES (?, ?, ?, ?)""",
               [stars_num, "message" + str(i), user_id, comic_id])

print("Stars done")

db.commit()
db.close()
