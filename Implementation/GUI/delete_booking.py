import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from table_display import *

class DeleteBookingWindow(QWidget):
    """this class creates a main window to delete bookings"""

    def __init__(self):
        super().__init__()
        self.display_table = DisplayTable()
        self.bookingtable = self.display_table.show_table("Menu")
        self.setWindowTitle("Delete Booking")
        self.setFixedSize(800,600)
        #create layouts
        self.main_layout = QVBoxLayout()
        self.input_layout = QHBoxLayout()

        self.main_layout.addWidget(self.bookingtable)
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
        self.setLayout(self.main_layout)


    def delete_booking(self):
        booking = self.input_bookingID.text()
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            sql = "delete from Booking where BookingID=?"
            cursor.execute(sql,booking)
            db.commit()
            
                             

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = DeleteBookingWindow()
    window.show()
    window.raise_()
    application.exec()

