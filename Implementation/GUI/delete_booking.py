import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DeleteBookingWindow(QMainWindow):
    """this class creates a main window to delete bookings"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Booking")
        self.setFixedSize(800,600)
        #create layouts
        self.main_layout = QVBoxLayout()
        self.input_layout = QHBoxLayout()

        self.main_layout.addLayout(self.input_layout)
        
        #create label
        self.bookingIDlabel = QLabel("Booking ID")
        self.bookingIDlabel.setMaximumSize(133,20)

        #line edit
        self.input_bookingID = QLineEdit()
        self.input_bookingID.setMaximumSize(self.input_bookingID.sizeHint())
        
        #create buttons
        self.delete_bookingID = QPushButton("Delete BookingID")
        self.delete_bookingID.setMaximumSize(133,20)
        self.delete_bookingID.clicked.connect(self.delete_booking)

        #add to input layout
        self.input_layout.addWidget(self.bookingIDlabel)
        self.input_layout.addWidget(self.input_bookingID)
        self.input_layout.addWidget(self.delete_bookingID)


        #create a widget to display main layout
        self.delete_booking_widget = QWidget()
        self.delete_booking_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.delete_booking_widget)

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

    def delete_booking(self):
        booking = self.input_bookingID.text()
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

