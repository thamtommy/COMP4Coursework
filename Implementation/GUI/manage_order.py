#http://pyqt.sourceforge.net/Docs/PyQt4/qdate.html#currentDate

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from table_display import *

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
        self.setWindowTitle("Manage Order")
        
        #create buttons
        self.back_button = QPushButton("Back") # Will be an arrow
        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete")
        self.finish_button = QPushButton("Finish")

        #connections


        #date widget


        #create labels
        self.drinks_label = QLabel("Drinks")
        self.dishes_label = QLabel("Dishes")
        self.table_number_label = QLabel("Table : {0} ".format(bookingDetails[3]))
        self.date_label = QLabel("Date : {0} ".format(bookingDetails[4]))
        self.time_label = QLabel("Time : {0} ".format(bookingDetails[5]))
        self.number_people_label = QLabel("Number of people : {0} ".format(bookingDetails[3]))
        
        #tables
        drinkQuery = """SELECT
                        Booking_Items.Quantity,
                        Items.ItemName,
                        Items.ItemPrice,
                        FROM Items INNER JOIN Booking_Items
                        ON Booking_Items.ItemID = Items.ItemID,
                        where BookingID = {0},
                        ItemTypeID = 2
                        """.format(bookingDetails[0])
        self.drinks_ordered_table = DisplayTable()
        self.drinks_ordered_table.show_results(drinkQuery)

        
        dishQuery = "ItemTypeID like '%1%' "
        self.dishes_ordered_table = DisplayTable()
        self.dishes_ordered_table.show_table(dishQuery)
        
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

        #widgets
        ##labels to drink/dish
        self.dishes_ordered.addWidget(self.dishes_label)
        self.drinks_ordered.addWidget(self.drinks_label)
        ##labels to order information
        self.order_information.addWidget(self.table_number_label)
        self.order_information.addWidget(self.date_label)
        self.order_information.addWidget(self.time_label)
        self.order_information.addWidget(self.number_people_label)
        ##table to drinks/dish
        self.drinks_ordered.addWidget(self.drinks_ordered_table)
        self.dishes_ordered.addWidget(self.dishes_ordered_table)



        #layouts
        ##add layouts to items ordered layout
        self.items_ordered.addLayout(self.dishes_ordered)
        self.items_ordered.addLayout(self.drinks_ordered)
        ##add layouts to main order layout
        self.order_layout.addLayout(self.order_information)
        self.order_layout.addLayout(self.items_ordered)
        self.order_layout.addLayout(self.manage_order)

        #create widget to display main order layout

        self.setLayout(self.order_layout)

    #def AddItem(self):
        self.exec_()
        
        

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = OrderWindow()
    window.show()
    window.raise_()
    application.exec()
