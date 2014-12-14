import sqlite3

def display_all_customers():
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Customer")
        customers = cursor.fetchall()
        print(customers)


def select_noOfppl(id):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("select NumberOfPeople from Customer where CustomerID=?",(id,))
        NoOfPpl = cursor.fetchone()
        print("The number of people is {0}.".format(NoOfPpl))

def select_tablenumber(id):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("select TableNumber from Customer where CustomerID=?",(id,))
        TableNo = cursor.fetchone()
        print("The table number is {0}.".format(TableNo))


def update_numberofpeople():
    display_all_customers()
    custID = int(input("Which Customer ID would you like to select: "))
    select_noOfppl(custID)
    
    newNumber = int(input("New number of people: "))
    data = (newNumber,custID)
    
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "update Customer set NumberOfPeople=? where CustomerID=?"
        cursor.execute("PRAGMA foreign_keys = ON") 
        cursor.execute(sql,data)
        db.commit()

def update_tablenumber():
    display_all_customers()
    custID = int(input("Which Customer ID would you like to select: "))
    select_tablenumber(custID)

    newTableNo = int(input("New table number: "))
    data = (newTableNo, custID)
    
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "update Customer set TableNumber=? where CustomerID=?"
        cursor.execute("PRAGMA foreign_keys = ON") 
        cursor.execute(sql,data)
        db.commit()
    

if __name__ == "__main__":
    update_numberofpeople()
    update_tablenumber()
