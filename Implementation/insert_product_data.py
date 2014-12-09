import sqlite3

def insert_data(values):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "insert into Menu (MenuItem,ItemPrice,ItemType) values (?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def get_menu_item():
    name = input("Enter name of item: ")
    price = float(input("Enter price of item: "))
    item_type = input("Enter type of item: ")
    menu_item = (name,price,item_type)
    insert_data(menu_item)

if __name__ == "__main__":
    get_menu_item()
    
