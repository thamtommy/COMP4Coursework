import sqlite3

#improvements

def display_all_reservations():
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Booking")
        reservations = cursor.fetchall()
        print(reservations)

def delete_Reservation():
    display_all_reservations()
    DeleteReservation = int(input("Which booking ID would you like to delete: "))
    
    
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "delete from Booking where BookingID=?"
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,DeleteReservation)
        db.commit()

if __name__ == "__main__":
    delete_Reservation()
                
