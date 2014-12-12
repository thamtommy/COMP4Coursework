import sqlite3

def select_data(values):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "select ItemPrice from Ordered_Items where OrderIemID=?"
        cursor.execute(sql,values)
        db.commit()

def get_OrderItemID():
    OrderItemID = int(input("Enter the ID for OrderID: "))


if __name__ == "__main__":
    get_ordered_items()
