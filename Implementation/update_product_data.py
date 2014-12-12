import sqlite3

def update_menu_item(data):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "update Menu set ItemPrice=? where MenuItem=?"
        cursor.execute("PRAGMA foreign_keys = ON") 
        cursor.execute(sql,data)
        db.commit()

def get_menu_item():
    itemName = input("Enter the name of the menu item that you would like to update: ")
    itemPrice = float(input("What do you want to update the price to: "))
    menu_item = (itemPrice,itemName)
    update_menu_item(menu_item)

if __name__ == "__main__":
    get_menu_item()
