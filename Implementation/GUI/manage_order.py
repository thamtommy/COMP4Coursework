#http://pyqt.sourceforge.net/Docs/PyQt4/qdate.html#currentDate

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from table_display import *
from add_item_to_order import *
from print_invoice import *

##        bookingID = bookingDetails[0]
##        customerID = bookingDetails[1]
##        tableNumber = bookingDetails[2]
##        numberPeople = bookingDetails[3]
##        Date = bookingDetails[4]
##        Time = bookingDetails[5]

class OrderWindow(QDialog):
    """this class creates a main window to observe the restaurant"""

    def __init__(self,bookingDetails):
        super().__init__()

        self.Finished = False
        
        self.setFixedSize(1000,500)
        self.setWindowTitle("Manage Order")
        self.bookingDetails = bookingDetails
        #create buttons
        self.back_button = QPushButton("Back") # Will be an arrow
        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete")
        self.finish_button = QPushButton("Finish")
        self.preview_invoice = QPushButton("Invoice Preview")
        self.invoice_button = QPushButton("Print Invoice")   

        #connections
        self.add_button.clicked.connect(self.AddItem)
        self.finish_button.clicked.connect(self.Finish)
        self.invoice_button.clicked.connect(self.Invoice)
        self.preview_invoice.clicked.connect(self.InvoicePreview)


        #create labels
        self.drinks_label = QLabel("Drinks")
        self.dishes_label = QLabel("Dishes")
        self.table_number_label = QLabel("Table : {0} ".format(bookingDetails[2]))
        self.date_label = QLabel("Date : {0} ".format(bookingDetails[4]))
        self.time_label = QLabel("Time : {0} ".format(bookingDetails[5]))
        self.number_people_label = QLabel("Number of people : {0} ".format(bookingDetails[3]))
        
        #tables
        self.drinkQuery = """SELECT
                        Booking_Items.Quantity,
                        Items.ItemName,
                        Items.ItemPrice
                        FROM Items
                        INNER JOIN Booking_Items
                        ON Booking_Items.ItemID = Items.ItemID
                        WHERE Booking_Items.BookingID = {0}
                        AND Items.ItemTypeID = 2
                        """.format(bookingDetails[0])
        self.drinks_ordered_table = DisplayTable()
        self.drinks_ordered_table.show_results(self.drinkQuery)

        
        self.dishQuery = """SELECT
                        Booking_Items.Quantity,
                        Items.ItemName,
                        Items.ItemPrice
                        FROM Items
                        INNER JOIN Booking_Items
                        ON Booking_Items.ItemID = Items.ItemID
                        WHERE Booking_Items.BookingID = {0}
                        AND Items.ItemTypeID = 1
                        """.format(bookingDetails[0])
        self.dishes_ordered_table = DisplayTable()
        self.dishes_ordered_table.show_results(self.dishQuery)
        
        
        #create layouts
        self.order_layout = QVBoxLayout()
        self.order_information = QHBoxLayout()
        self.items_ordered = QHBoxLayout()
        self.dishes_ordered = QVBoxLayout()
        self.drinks_ordered = QVBoxLayout()
        self.manage_order = QHBoxLayout()

        #add buttons to layouts
        self.manage_order.addWidget(self.add_button)
        self.manage_order.addWidget(self.delete_button)
        self.manage_order.addWidget(self.finish_button)
        self.manage_order.addWidget(self.preview_invoice)
        self.manage_order.addWidget(self.invoice_button)

        self.dishes_ordered.addWidget(self.dishes_label)
        self.drinks_ordered.addWidget(self.drinks_label)

        self.order_information.addWidget(self.table_number_label)
        self.order_information.addWidget(self.date_label)
        self.order_information.addWidget(self.time_label)
        self.order_information.addWidget(self.number_people_label)

        self.drinks_ordered.addWidget(self.drinks_ordered_table)
        self.dishes_ordered.addWidget(self.dishes_ordered_table)

        self.items_ordered.addLayout(self.dishes_ordered)
        self.items_ordered.addLayout(self.drinks_ordered)
        ##add layouts to main order layout
        self.order_layout.addLayout(self.order_information)
        self.order_layout.addLayout(self.items_ordered)
        self.order_layout.addLayout(self.manage_order)

        self.setLayout(self.order_layout)

        self.adjustSize
        self.exec_()

    def AddItem(self):
        self.AddOrderItem = AddItemToMenu(self.bookingDetails)        
        self.AddOrderItem.exec_()
        self.AddOrderItem.itemAdded.connect(self.refreshQuery)
        

    def refreshQuery(self):
        self.dishes_ordered_table.show_results(self.dishQuery).exec_()
        self.dishes_ordered_table.show_results(self.drinkQuery).exec_()

    def Finish(self):
        self.Finished = True
        self.close()
        return self.Finished

    def Invoice(self):
        self.Invoice = CustomerInvoice(self.bookingDetails)
        self.Invoice.print_invoice()

    def InvoicePreview(self):
        self.Invoice = CustomerInvoice(self.bookingDetails)
        self.Invoice.print_preview()
        

    
        
        
        
        

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = OrderWindow()
    window.show()
    window.raise_()
    application.exec()
