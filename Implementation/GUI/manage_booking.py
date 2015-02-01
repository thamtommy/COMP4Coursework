#http://pyqt.sourceforge.net/Docs/PyQt4/qdate.html#currentDate

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from add_booking import*
from delete_booking import*
from table_display import *

class BookingWindow(QWidget):
    """this class creates a window to observe the bookings"""

    def __init__(self):
        super().__init__()

        #create layouts
        self.manage_booking = QHBoxLayout()


        #create buttons
        self.back_button = QPushButton("Back") # Will be an arrow
        self.add_button = QPushButton("Add Booking")
        self.delete_button = QPushButton("Delete Booking")

        #add buttons to layouts
        self.manage_booking.addWidget(self.add_button)
        self.manage_booking.addWidget(self.delete_button)

        #create widget to display main booking layout

        self.setLayout(self.manage_booking)

        #set layout to stacked layout

        



    def refresh_database(self):
        self.display_widget = DisplayTable()
        print("refresh")
        self.display_widget.refresh()
        




if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = BookingWindow()
    window.show()
    window.raise_()
    application.exec()
