#http://pyqt.sourceforge.net/Docs/PyQt4/qdate.html#currentDate

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from table_display import *

class BookingWindow(QWidget):
    """this class creates a widget to observe the bookings"""

    def __init__(self):
        super().__init__()

        #create layouts
        self.manage_layout = QVBoxLayout()
        self.manage_booking = QHBoxLayout()

        #create buttons
        self.back_button = QPushButton("Back") 
        self.add_button = QPushButton("Add Booking")
        self.delete_button = QPushButton("Delete Booking")

        #add buttons to layouts
        self.manage_booking.addWidget(self.add_button)
        self.manage_booking.addWidget(self.delete_button)

        self.display_booking_table = DisplayTable()
        self.display_booking_table.show_table("Bookings")

        self.manage_layout.addWidget(self.display_booking_table)
        self.manage_layout.addLayout(self.manage_booking)
        self.setLayout(self.manage_layout)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = BookingWindow()
    window.show()
    window.raise_()
    application.exec()
