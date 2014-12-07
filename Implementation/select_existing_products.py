import sqlite3

def select_all_products():
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Menu")
        menu_items = cursor.fetchall()
        return menu_items

def select_product(id):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("select MenuItem, ItemPrice from Menu where MenuID=?",(id,))
        menu_item = cursor.fetchone()
        return menu_item

if __name__ == "__main__":
    menu_items = select_all_products()
    print(menu_items)
    menu_item = select_product(3)
    print(menu_item)
