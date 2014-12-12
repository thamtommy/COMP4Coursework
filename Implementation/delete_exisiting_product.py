import sqlite3

def delete_menu_item(data):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "delete from Menu where MenuItem=?"
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()
        
def get_menu_item():
    item = input("Product to delete: ")
    item = (item,)
    delete_menu_item(item)

if __name__ == "__main__":
    get_menu_item()
