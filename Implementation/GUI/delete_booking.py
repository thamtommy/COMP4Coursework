import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DeleteBookingWindow(QMainWindow):
    """this class creates a main window to delete bookings"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Booking")
        self.create_delete_booking_layout()
        self.setFixedSize(800,600)

    def create_tool_bar(self):
        #create toolbar
        self.main_screen_tool_bar = QToolBar()
        self.orders_tool_bar = QToolBar()
        self.bookings_tool_bar = QToolBar()

        self.main_screen_label_bar = QPushButton("Main Screen")
        self.main_screen_label_bar.setToolTip("This will direct you to main screen")
        self.orders_label_bar = QPushButton("Orders")
        self.orders_label_bar.setToolTip("All orders will be displayed")
        self.bookings_label_bar = QPushButton("Bookings")
        self.bookings_label_bar.setToolTip("All bookings will be displayed")

        self.main_screen_tool_bar.addWidget(self.main_screen_label_bar)
        self.orders_tool_bar.addWidget(self.orders_label_bar)
        self.bookings_tool_bar.addWidget(self.bookings_label_bar)
        

        self.addToolBar(self.main_screen_tool_bar)
        self.addToolBar(self.orders_tool_bar)
        self.addToolBar(self.bookings_tool_bar)

    def display_booking_database(self):


    def create_delete_booking_layout(self):
        #methods

        #create layouts
        self.main_layout = QVBoxLayout()        
        
        #create buttons
        self.add_complete = QPushButton("Delete Booking")


        #create a widget to display main layout
        self.delete_booking_widget = QWidget()
        self.delete_booking_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.delete_booking_widget)

        #connections

    def delete_booking(self):
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            sql = "delete from Booking where BookingID=?"
            cursor.execute(sql,booking)
            db.commit()
            
                             

def main():
    restaurant_simulation = QApplication(sys.argv) # create new application
    restaurant_window = DeleteBookingWindow() #create new instance of main window
    restaurant_window.show() #make instance visible
    restaurant_window.raise_() #raise instance to top of window stack
    restaurant_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()

