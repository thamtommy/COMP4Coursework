import sqlite3

def delete_ordered_itemID():
    itemID = int(input("Which order itemID would you like to delete: "))

    data = (itemID,)
    
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "delete from Ordered_Items where OrderItemID=?"
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    delete_ordered_itemID()
