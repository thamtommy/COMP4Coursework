import sqlite3

def insert_data(values):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "insert into Booking (FirstName,LastName,TelephoneNo,BookingTime,BookingDate) values (?,?,?,?,?)"
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,values)
        db.commit()

def get_booking_details():
    FName = input("Enter first name: ")
    LName = input("Enter last name: ")
    TeleNo = input("Enter telephone number: ")
    RTime = input("Enter booking time: ")
    RDate = input("Enter booking date: ")
    booking = (FName,LName,TeleNo,RTime,RDate)
    insert_data(booking)

if __name__ == "__main__":
    get_booking_details()

    

