import sqlite3
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *



class BookingWindow(QWidget):
    """this class creates a window to observe the bookings"""

    def __init__(self):
        super().__init__()

        self.main_assign_layout = QVBoxLayout()
        self.choose_customer = QHBoxLayout()
        self.create_combo_box()
        
        #add buttons to layouts
        self.choose_customer.addWidget(self.customer_combo_box)
        
        self.select_customer = QPushButton("Select")
        self.choose_customer.addWidget(self.select_customer)
        self.select_customer.clicked.connect(self.select_connect)

        self.street_customer = QPushButton("Random Street Customer")
        #self.street_customer.clicked.connect(self.select_random_connect)

        self.main_assign_layout.addLayout(self.choose_customer)
        self.main_assign_layout.addWidget(self.street_customer)
                                        

        self.setLayout(self.main_assign_layout)



    def select_connect(self):
        customerCurrentIndex = self.customer_combo_box.currentIndex()
        print("Customer : {0}".format(customerCurrentIndex))
        self.CustomerList[customerCurrentIndex]
        print("Customer ID: {0}".format(self.CustomerList[customerCurrentIndex]))
        
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Bookings where CustomerID = {0}".format(customerCurrentIndex))
            bookingDetails = cursor.fetchone()         
            print(bookingDetails)        

    def create_combo_box(self):
        CustomerList = []
        CustomerLastName = []

        ## get all customer IDs that are on table _
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("select CustomerID from Bookings where TableNumber = 1")#.format(self.TableNumber))
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
        self.customer_combo_box = QComboBox(self)
        for each in CustomerLastName:
            self.customer_combo_box.addItem(each)

        self.CustomerList = CustomerList





if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = BookingWindow()
    window.show()
    window.raise_()
    application.exec()
