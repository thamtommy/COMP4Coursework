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

def delete_menu_itemID(data):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "delete from Menu where MenuID=?"
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()

def delete_itemtype(data):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "delete from ItemType where ItemTypeID=?"
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()

def get_menu_item():
    item = input("Product to delete: ")
    item = (item,)
    delete_menu_item(item)

def get_menu_itemID():
    itemID = int(input("Menu item ID to delete: "))
    itemID = (itemID,)
    delete_menu_itemID(itemID)

def Options():
    print("Would you like to: ")
    print('')
    print("1. Delete a menu item by its name")
    print("2. Delete a menu item by its ID")
    print('')
    option = int(input('Choice : '))
    return option

if __name__ == "__main__":
<<<<<<< HEAD
    get_menu_item()
=======
    option = Options()
    if option == 1:
        get_menu_item()
    elif option == 2:
        get_menu_itemID()

>>>>>>> branch 'master' of https://github.com/thamtommy/COMP4Coursework.git
