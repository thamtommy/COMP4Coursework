import sqlite3

#improvements
#add a verification ( "are you sure you want to delete {0}? "

def display_all_reservations():
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Reservation")
        reservations = cursor.fetchall()
        print(reservations)

def delete_Reservation():
    display_all_reservations()
    DeleteReservation = int(input("Which reservation ID would you like to delete: "))
    
    
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "delete from Reservation where ReservationID=?"
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,DeleteReservation)
        db.commit()

if __name__ == "__main__":
    delete_Reservation()
                
