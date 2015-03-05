import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from table_display import *
from print_invoice import *

class SearchOrder(QWidget):
    """this class will be used to search for orders using booking IDs"""

    def __init__(self):
        super().__init__()
        booking = None
        self.setWindowTitle("Delete Booking")       
        self.items_ordered_table = DisplayTable()
        self.items_ordered_table.setFixedWidth(350)

 

        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.input_layout = QGridLayout()

    
        self.display_table = DisplayTable()
        self.display_table.show_table("Bookings")
        self.display_table.setFixedWidth(690)
        self.bookingIDlabel = QLabel("Booking ID")
        self.bookingIDlabel.setMaximumSize(100,20)

        regexp = QRegExp("^\\d\\d\\d?$")
        validator = QRegExpValidator(regexp)
        self.input_bookingID = QLineEdit()
        self.input_bookingID.setValidator(validator)
        self.input_bookingID.setMaximumSize(self.input_bookingID.sizeHint())
        self.search_bookingID = QPushButton("Search Order")
        self.search_bookingID.setMaximumSize(133,20)
        self.search_bookingID.clicked.connect(self.search_order)

        self.preview_button = QPushButton("Preview Invoice")
        self.preview_button.setMaximumSize(133,20)
        self.preview_button.clicked.connect(self.preview_invoice)

        self.print_button = QPushButton("Print Invoice")
        self.print_button.setMaximumSize(133,20)
        self.print_button.clicked.connect(self.invoice_print)
        
        self.input_layout.addWidget(self.bookingIDlabel,0,0)
        self.input_layout.addWidget(self.input_bookingID,0,1)
        self.input_layout.addWidget(self.search_bookingID,0,2)
        self.input_layout.addWidget(self.preview_button,1,1)
        self.input_layout.addWidget(self.print_button,2,1)

        self.top_layout.addWidget(self.display_table)
        self.top_layout.addLayout(self.input_layout)
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addWidget(self.items_ordered_table)
        self.setLayout(self.main_layout)


    def search_order(self):
        self.booking = self.input_bookingID.text()
        self.searchQuery = """SELECT
                        Booking_Items.Quantity,
                        Items.ItemName,
                        Items.ItemPrice
                        FROM Items
                        INNER JOIN Booking_Items
                        ON Booking_Items.ItemID = Items.ItemID
                        WHERE Booking_Items.BookingID = {0}
                        """.format(self.booking) 
        self.items_ordered_table.show_results(self.searchQuery)


            

    def preview_invoice(self):
        
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Bookings where BookingID = {0} ".format(self.booking))
            bookingDetails = cursor.fetchone()
            
        self.invoice = CustomerInvoice(bookingDetails)
        self.invoice.print_preview()

    def invoice_print(self):

        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Bookings where BookingID = {0} ".format(self.booking))
            bookingDetails = cursor.fetchone()

        self.invoice = CustomerInvoice(bookingDetails)
        self.invoice.print_invoice()
        


            
                             

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = DeleteBookingWindow()
    window.show()
    window.raise_()
    application.exec()

