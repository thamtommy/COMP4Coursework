#http://pyqt.sourceforge.net/Docs/PyQt4/qdate.html#currentDate

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from add_booking2 import *
from delete_booking2 import *

class BookingWindow(QWidget):
    """this class creates a window to observe the bookings"""

    def __init__(self):
        super().__init__()

        #create layouts
        self.booking_layout = QVBoxLayout()
        self.view_bookings = QGridLayout()
        self.manage_booking = QHBoxLayout()
        self.stacked_layout = QStackedLayout()

        #create buttons
        self.back_button = QPushButton("Back") # Will be an arrow
        self.add_button = QPushButton("Add Booking")
        self.delete_button = QPushButton("Delete Booking")

        #add buttons to layouts
        self.manage_booking.addWidget(self.add_button)
        self.manage_booking.addWidget(self.delete_button)


        #add layouts to main booking layout
        self.booking_layout.addLayout(self.view_bookings)
        self.booking_layout.addLayout(self.manage_booking)

        #create widget to display main booking layout
        self.view_booking_widget = QWidget()
        self.view_booking_widget.setLayout(self.booking_layout)

        #add main layout to stack
        self.stacked_layout.addWidget(self.view_booking_widget)

        #set layout to stacked layout
        self.setLayout(self.stacked_layout)
        self.stacked_layout.setCurrentIndex(0)

        #stacked layout
        self.add_booking_widget = AddBookingWindow()#import from addbooking.py
        self.stacked_layout.addWidget(self.add_booking_widget)#got layout from main program of addbooking.py

        self.delete_booking_widget = DeleteBookingWindow()
        self.stacked_layout.addWidget(self.delete_booking_widget)
        
        #connections
        self.add_button.clicked.connect(self.add_booking_connection)
        self.delete_button.clicked.connect(self.delete_booking_connection)

    def add_booking_connection(self):       
        self.stacked_layout.setCurrentIndex(1)

    def delete_booking_connection(self):
        self.stacked_layout.setCurrentIndex(2)



if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = BookingWindow()
    window.show()
    window.raise_()
    application.exec()
