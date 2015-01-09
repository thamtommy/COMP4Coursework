#http://pyqt.sourceforge.net/Docs/PyQt4/qdate.html#currentDate

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from add_booking import*
from radio_button_widget_class import *

class BookingWindow(QMainWindow):
    """this class creates a window to observe the bookings"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage Booking")
        self.create_manage_booking_layout()

        self.booking_stacked_layout = QStackedLayout()
        self.booking_stacked_layout.addWidget(self.view_booking_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.booking_stacked_layout)
        self.setCentralWidget(self.central_widget)
        
        
    def create_manage_booking_layout(self):
        #create buttons
        self.back_button = QPushButton("Back") # Will be an arrow
        self.add_button = QPushButton("Add Booking")
        self.delete_button = QPushButton("Delete Booking")

        
        #create layouts
        self.booking_layout = QVBoxLayout()
        self.view_bookings = QGridLayout()
        self.manage_booking = QHBoxLayout()

        #add buttons to layouts
        self.manage_booking.addWidget(self.add_button)
        self.manage_booking.addWidget(self.delete_button)


        #add layouts to main booking layout
        self.booking_layout.addLayout(self.view_bookings)
        self.booking_layout.addLayout(self.manage_booking)

        #create widget to display main order layout
        self.view_booking_widget = QWidget()
        self.view_booking_widget.setLayout(self.booking_layout)

        #connections
        self.add_button.clicked.connect(self.add_booking)

    def add_booking(self):
        self.add_booking = AddBookingWindow()#import from addbooking.py
        self.booking_stacked_layout.addWidget(self.add_booking)#got layout from main program of addbooking.py
        self.booking_stacked_layout.setCurrentIndex(1) #change layout to add booking layout


def main():
    booking_manage = QApplication(sys.argv) # create new application
    booking_window = BookingWindow() #create new instance of main window
    booking_window.show() #make instance visible
    booking_window.raise_() #raise instance to top of window stack
    booking_manage.exec_() #monitor application for events

if __name__ == "__main__":
    main()

