import sqlite3

def insert_data(values):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "insert into Reservation (FirstName,LastName,TelephoneNo,BookingTime,BookingDate) values (?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def get_booking_details():
    FName = input("Enter first name: ")
    LName = input("Enter last name: ")
    TeleNo = input("Enter telephone number: ")
    BTime = input("Enter booking time: ")
    BDate = input("Enter booking date: ")
    booking = (FName,LName,TeleNo,BTime,BDate)
    insert_data(booking)

if __name__ == "__main__":
    get_booking_details()
    
