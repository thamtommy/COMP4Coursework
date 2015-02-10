import sqlite3
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from off_the_street_booking import *



class AssignCustomer(QDialog):
    """this class creates a window to observe the bookings"""

    def __init__(self,TableNumber):
        super().__init__()

        

        self.random_customer = RandomCustomer(TableNumber)
        self.random_customer_layout = self.random_customer.main_layout
        

        self.main_assign_layout = QVBoxLayout()
        self.choose_customer = QHBoxLayout()
        self.create_combo_box(TableNumber)
        
        #add buttons to layouts
        self.choose_customer.addWidget(self.customer_combo_box)
        
        self.select_customer = QPushButton("Select")
        self.choose_customer.addWidget(self.select_customer)
        self.select_customer.clicked.connect(self.select_connect)

        self.street_customer = QPushButton("Random Street Customer")
        self.street_customer.clicked.connect(self.select_random_connect)

        self.main_assign_layout.addLayout(self.choose_customer)
        self.main_assign_layout.addWidget(self.street_customer)
                                        

        self.setLayout(self.main_assign_layout)

        
        
        self.exec_()

    def select_random_connect(self):
        print("CONNECT")
        self.setLayout(self.random_customer_layout)



    def select_connect(self):
        customerCurrentIndex = self.customer_combo_box.currentIndex()
        print("Customer : {0}".format(customerCurrentIndex))
        CustomerID = self.CustomerList[customerCurrentIndex]
        print("Customer ID: {0}".format(CustomerID))
        
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Bookings where CustomerID = {0}".format(CustomerID))
            bookingDetails = cursor.fetchone()         
            print(bookingDetails)

        bookingID = bookingDetails[0]
        customerID = bookingDetails[1]
        tableNumber = bookingDetails[2]
        numberPeople = bookingDetails[3]
        Date = bookingDetails[4]
        Time = bookingDetails[5]

    def create_combo_box(self,TableNumber):
        self.CustomerList = []
        CustomerLastName = []

        ## get all customer IDs that are on table _
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("select CustomerID from Bookings where TableNumber = {0}".format(TableNumber))
            customers = cursor.fetchall()
            for each in customers:
                self.CustomerList.append(each[0])          
            print(self.CustomerList)

        ## get all last names from previouse fetchall 
        for customer in self.CustomerList:
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

        
        




if __name__ == "__main__":
    TableNumber = 1
    application = QApplication(sys.argv)
    window = AssignCustomer(TableNumber)
    window.show()
    window.raise_()
    application.exec()
