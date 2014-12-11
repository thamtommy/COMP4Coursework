import sqlite3
import time
import datetime

def insert_data(values):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "insert into Customer (NumberOfPeople,Date,Time,TableNumber) values (?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def get_customer_details():
    NumberOfPeople = int(input("Number of people: "))
    Date = datetime.date.today()
    Time = time.localtime(time.time())
    TableNumber = int(input("Table Number: "))
    customer = (NumberOfPeople,Date,Time,TableNumber)
    insert_data(customer)

if __name__ == "__main__":
    get_customer_details()
    
            
