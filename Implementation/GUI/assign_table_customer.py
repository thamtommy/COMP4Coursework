import sqlite3
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from table_display import *
import time

class AssignCustomer(QDialog):
    """this class creates a window to observe the bookings"""

    def __init__(self,TableNumber):
        super().__init__()
        self.setWindowTitle("Assign customer to table {0}".format(TableNumber))
        self.setMinimumSize(600,600)
        self.tableNumber = TableNumber

        self.titleFont = QFont()
        self.titleFont.setPointSize(15)


        self.todays_bookings_label = QLabel("Todays bookings for table {0}".format(TableNumber))
        self.todays_bookings_label.setFont(self.titleFont)
        self.todays_bookings_label.setAlignment(Qt.AlignLeft)
        self.todays_bookings_label.setFixedWidth(400)


        self.main_assign_layout = QVBoxLayout()
        self.choose_customer = QHBoxLayout()
        self.create_combo_box(TableNumber)
        self.add_customer_layout = QGridLayout()
        self.create_complete_layout = QHBoxLayout()
        

        self.choose_customer.addWidget(self.customer_combo_box)
        self.select_customer = QPushButton("Select")
        self.choose_customer.addWidget(self.select_customer)
        self.select_customer.clicked.connect(self.select_connect)        
        
        #create buttons
        self.create_complete = QPushButton("Create")
        self.create_complete.clicked.connect(self.create_booking)
        
        #labels
        self.table_number_label = QLabel("Table Number : ")
        self.number_of_people_label = QLabel("Number Of People : ")
        self.time_arrived_label = QLabel("Time Of Arrival : ")
        self.date_arrived_label = QLabel("Date Of Arrival : ")

        self.systemtime = time.strftime("%H:%M")
        self.system_time_label = QLineEdit(self.systemtime)
        self.system_time_label.setReadOnly(True)
        sizehint = self.system_time_label.sizeHint()
        self.system_time_label.setMaximumSize(sizehint)

        self.systemdate = time.strftime("%d/%m/%Y")
        self.system_date_label = QLineEdit(self.systemdate)
        self.system_date_label.setReadOnly(True)
        self.system_date_label.setMaximumSize(sizehint)

        self.display_table_number = QLineEdit("{0}".format(TableNumber))
        self.display_table_number.setReadOnly(True)
        self.display_table_number.setMaximumSize(sizehint)

        regexp = QRegExp("^\\d\\d?$")
        validator = QRegExpValidator(regexp)
        self.input_number_of_people = QLineEdit()
        self.input_number_of_people.setValidator(validator)
        self.input_number_of_people.setMaximumSize(sizehint)


        displayQuery = """SELECT
                        Customers.FirstName,
                        Customers.LastName,
                        Bookings.NumberOfPeople,
                        Bookings.Time
                        FROM Customers
                        INNER JOIN Bookings
                        ON Customers.CustomerID = Bookings.CustomerID
                        WHERE Bookings.Date = '{0}'
                        AND Bookings.TableNumber = {1}
                        """.format(self.systemdate,TableNumber)

        self.display_customers = DisplayTable()
        self.display_customers.show_results(displayQuery)


        self.add_customer_layout.addWidget(self.table_number_label,0,0)
        self.add_customer_layout.addWidget(self.display_table_number,0,1)
        self.add_customer_layout.addWidget(self.time_arrived_label,1,0)
        self.add_customer_layout.addWidget(self.date_arrived_label,2,0)
        self.add_customer_layout.addWidget(self.system_time_label,1,1)
        self.add_customer_layout.addWidget(self.system_date_label,2,1)
        self.add_customer_layout.addWidget(self.number_of_people_label,3,0)
        self.add_customer_layout.addWidget(self.input_number_of_people,3,1)
        self.add_customer_layout.addWidget(self.create_complete,4,0,2,2)  
        #add layouts to main layout

        self.assign_street_box = QGroupBox("Customer that has not booked in advance")
        self.assign_street_box.setLayout(self.add_customer_layout)

        self.assign_booked_box = QGroupBox("Customer that has booked in advance")
        self.assign_booked_box.setLayout(self.choose_customer)

        self.main_assign_layout.addWidget(self.todays_bookings_label)
        self.main_assign_layout.addWidget(self.display_customers)
        self.main_assign_layout.addWidget(self.assign_booked_box)
        self.main_assign_layout.addWidget(self.assign_street_box)                          
        self.setLayout(self.main_assign_layout)
        
        self.exec_()

    def create_booking(self):
        TableNumber = self.display_table_number.text()

        #create bookingID for customer
        CustomerID = 1
        NumberOfPeople = self.input_number_of_people.text()
        Date = self.systemdate
        Time = self.systemtime
       

        Booking = (CustomerID,TableNumber,NumberOfPeople,Date,Time)

        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            sql = "insert into Bookings(CustomerID,TableNumber,NumberOfPeople,Date,Time) values (?,?,?,?,?)"
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql,Booking)
            db.commit()
            
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Bookings where CustomerID = {0} and TableNumber = {1} and NumberOfPeople = {2} and Date = '{3}' and Time = '{4}' ".format(CustomerID,TableNumber,NumberOfPeople,Date,Time))
            self.bookingDetails = cursor.fetchone()

        self.close()
        return self.bookingDetails

    def select_connect(self):
        TodaysDate = time.strftime("%d/%m/%Y")
        customerCurrentIndex = self.customer_combo_box.currentIndex()
        print("Customer : {0}".format(customerCurrentIndex))
        CustomerID = self.CustomerList[customerCurrentIndex]
        print("Customer ID: {0}".format(CustomerID))
        
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Bookings where CustomerID = {0} and TableNumber = {1} and Date = '{2}'".format(CustomerID,self.tableNumber,TodaysDate))
            self.bookingDetails = cursor.fetchone()         
            print(self.bookingDetails)

        self.close()
        
        return self.bookingDetails

    def create_combo_box(self,TableNumber):
        self.CustomerList = []
        CustomerLastName = []
        TodaysDate = time.strftime("%d/%m/%Y")

        ## get all customer IDs that are on table _
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("select CustomerID from Bookings where TableNumber = {0} and Date = '{1}'".format(TableNumber,(TodaysDate)))
            customers = cursor.fetchall()
            for each in customers:
                self.CustomerList.append(each[0])          

        ## get all last names from previouse fetchall 
        for customer in self.CustomerList:
            with sqlite3.connect("restaurant.db") as db:
                cursor = db.cursor()
                cursor.execute("select LastName from Customers where CustomerID = {0}".format(customer))
                customer = cursor.fetchone()
                CustomerLastName.append(customer[0]) 
            
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
