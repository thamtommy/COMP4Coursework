import sqlite3

def insert_data(values):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "insert into Menu (MenuItem, ItemPrice) values (?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    menu_item = ("Americano", 1.50)
    insert_data(menu_item)
