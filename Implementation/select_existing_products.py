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

def get_product():
    menuid = int(input("Enter a menuid: "))
    return menuid

def Options():
    print("Would you like to: ")
    print('')
    print("1. Look at all the menu items")
    print("2. Search for a particular menu item")
    print('')
    option = int(input(''))
    return option

if __name__ == "__main__":
    option = Options()
    if option == 1:
        menu_items = select_all_products()
        print(menu_items)
    elif option == 2:
        menuid = get_product()
        menu_item = select_product(menuid)
        print(menu_item)
