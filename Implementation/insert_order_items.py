import sqlite3

def insert_data(values):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "insert into Ordered_Items (OrderID,MenuID,Quantity) values (?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def get_ordered_items():
    orderID = int(input("Enter OrderID: "))
    item = int(input("Enter menu item ID: "))
    menu_item = select_product(item)
    quantity = int(input("How many of {0} has been ordered: ".format(menu_item)))
    insert_data(orderID,item,quantity)

def insert_orderID():
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "insert into Orders(TotalDrinkPrice,TotalDishPrice,TotalPrice) values (?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def initial_orderID_data():
    TotalDrinkPrice = 0
    TotalDishPrice = 0
    TotalPrice = TotalDrinkPrice + TotalDishPrice
    insert_orderID(TotalDrinkPrice,TotalDishPrice,TotalPrice)

def select_product(id):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("select MenuItem from Menu where MenuID=?",(id,))
        menu_item = cursor.fetchone()
        return menu_item



if __name__ == "__main__":
    get_ordered_items()
