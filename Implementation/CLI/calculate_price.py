import sqlite3

def get_data():
    OrderID = int(input("Enter the ID for OrderID: "))
    

    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("select MenuID from Ordered_Items where OrderID=?",(OrderID,))
        menuID = cursor.fetchone()
        return menuID

def get_price(menuID)
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("select ItemPrice from Menu where MenuID=?",(menuID,)
        menuID_price = cursor.fetchone()
        return menuID_price

def add_price(menuID_price):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "insert into Orders (TotalDishPrice) values (?)"
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,menuID_price)
        db.commit()


if __name__ == "__main__":
    menuID = get_data()
    menuID_price = get_price(menuID)
    add_price(menuID_price)
                       
    
