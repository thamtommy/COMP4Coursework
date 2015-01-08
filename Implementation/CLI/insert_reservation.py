import sqlite3

def insert_data(values):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "insert into Reservation (FirstName,LastName,TelephoneNo,ReservationTime,ReservationDate) values (?,?,?,?,?)"
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,values)
        db.commit()

def get_reservation_details():
    FName = input("Enter first name: ")
    LName = input("Enter last name: ")
    TeleNo = input("Enter telephone number: ")
    RTime = input("Enter reservation time: ")
    RDate = input("Enter reservation date: ")
    reservation = (FName,LName,TeleNo,RTime,RDate)
    insert_data(reservation)

if __name__ == "__main__":
    get_reservation_details()

    

