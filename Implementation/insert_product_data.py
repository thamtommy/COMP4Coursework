import sqlite3

def insert_data(values):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
<<<<<<< HEAD
        sql = "insert into Menu (MenuItem,ItemPrice,ItemType) values (?,?,?)"
=======
        sql = "insert into Menu (MenuItem,ItemPrice,ItemTypeID) values (?,?,?)"
>>>>>>> branch 'master' of https://github.com/thamtommy/COMP4Coursework.git
        cursor.execute(sql,values)
        db.commit()

def insert_type(values):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
<<<<<<< HEAD
        sql = "insert into ItemType (ItemType) values (?)"
        cursor.execute(sql,values)
        db.commit()

def get_menu_item():
    name = input("Enter name of item: ")
    price = float(input("Enter price of item: "))
    item_type = input("Enter type of item: ")
=======
        sql = "insert into ItemType(Type) values (?)"
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,values)
        db.commit()

def ItemType():
    insert_type(("Drink",))
    insert_type(("Dish",))

def get_menu_item():
    name = input("Enter name of item: ")
    price = float(input("Enter price of item: "))
    item_type = int(input("Enter type of item(1 for drink, 2 for dish) : "))
>>>>>>> branch 'master' of https://github.com/thamtommy/COMP4Coursework.git
    menu_item = (name,price,item_type)
    insert_data(menu_item)

if __name__ == "__main__":
<<<<<<< HEAD
    get_menu_item()
=======
    ItemType()
    get_menu_item()
    
>>>>>>> branch 'master' of https://github.com/thamtommy/COMP4Coursework.git
