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

        self.choose_customer = QHBoxLayout()
        self.create_combo_box()
        
        #add buttons to layouts
        self.choose_customer.addWidget(self.select_customer)


        self.setLayout(self.choose_customer)

    def create_combo_box(self):
        CustomerList = []
        CustomerLastName = []

        ## get all customer IDs that are on table _
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("select CustomerID from Bookings where TableNumber = {0}".format(self.TableNumber))
            customers = cursor.fetchall()
            for each in customers:
                CustomerList.append(each[0])          
            print(CustomerList)

        ## get all last names from previouse fetchall 
        for customer in CustomerList:
            with sqlite3.connect("restaurant.db") as db:
                cursor = db.cursor()
                cursor.execute("select LastName from Customers where CustomerID = {0}".format(customer))
                customer = cursor.fetchone()
                CustomerLastName.append(customer[0]) 

        print(CustomerLastName)
            
        #create combo, insert all last names from fetchall
        self.select_customer = QComboBox(self)
        for each in CustomerLastName:
            self.select_customer.addItem(each)
        





if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = BookingWindow()
    window.show()
    window.raise_()
    application.exec()
