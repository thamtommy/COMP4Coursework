import sqlite3

def query(sql,data):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    sql = "delete from ProductType where Description = 'Tea'"
    query(sql,())
