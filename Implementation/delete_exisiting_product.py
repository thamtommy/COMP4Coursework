import sqlite3

def delete_product(data):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "delete from Menu where MenuItem=?"
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    data = ("Latte",)
    delete_product(data)
