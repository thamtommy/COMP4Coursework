import sqlite3

def update_product(data):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "update Menu set MenuItem=?, ItemPrice=? where MenuID=?"
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    data = ("Latte", 2.45,1)
    update_product(data)
