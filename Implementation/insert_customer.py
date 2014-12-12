import sqlite3
import time
import datetime

def insert_data(values):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "insert into Customer (NumberOfPeople,Date,Time,TableNumber) values (?,?,?,?)"
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,values)
        db.commit()

def get_customer_details():
    NumberOfPeople = int(input("Number of people: "))
    Date = datetime.date.today()
    Time = ("Time") # temporary
    TableNumber = int(input("Table Number: "))
    customer = (NumberOfPeople,Date,Time,TableNumber)
    insert_data(customer)

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

if __name__ == "__main__":
    get_customer_details()
    
            

