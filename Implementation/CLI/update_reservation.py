import sqlite3

def update_reservation_time():
    display_all_reservations()
    ResID = int(input("Which Booking ID would you like to update: "))
    display_reservation_time(ResID)

    newTime = input("Enter new time: ")
    data = (newTime,ResID)
    
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "update Booking set BookingTime=? where BookingID=?"
        cursor.execute("PRAGMA foreign_keys = ON") 
        cursor.execute(sql,data)
        db.commit()

def update_reservation_date():
    display_all_reservations()
    ResID = int(input("Which Booking ID would you like to update: "))
    display_reservation_date(ResID)

    newDate = input("Enter new date: ")
    data = (newDate,ResID)
    
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "update Booking set BookingDate=? where BookingID=?"
        cursor.execute("PRAGMA foreign_keys = ON") 
        cursor.execute(sql,data)
        db.commit()

def display_all_reservations():
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Booking")
        reservations = cursor.fetchall()
        print(reservations)

def display_reservation_time(id):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("select BookingTime from Booking where BookingID=?",(id,))
        RTime = cursor.fetchone()
        print("The current reservation time is {0} for Booking ID {1}.".format(RTime,ResID))

def display_reservation_date(id):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("select BookingDate from Booking where BookingID=?",(id,))
        RDate = cursor.fetchone()
        print("The current reservation date is {0} for reservation ID {1}.".format(RDate,ResID))    

if __name__ == "__main__":
    update_reservation_date()
    update_reservation_time()
