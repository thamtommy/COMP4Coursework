import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
import pdb


class RandomCustomer(QWidget):
    """this class creates a window to add bookings"""
    bookingCreated = pyqtSignal()

    def __init__(self,TableNumber):
        super().__init__()
        self.setMaximumSize(1000,1000)
        #methods

        #create layouts
        self.main_layout = QVBoxLayout()
        self.add_customer_layout = QGridLayout()
        self.create_complete_layout = QHBoxLayout()
        
        
        #create buttons
        self.create_complete = QPushButton("Create")
        
        #labels
        self.table_number_label = QLabel("Table Number : ")
        self.number_of_people_label = QLabel("Number Of People : ")
        self.time_arrived_label = QLabel("Time Of Arrival : ")
        self.date_arrived_label = QLabel("Date Of Arrival : ")

        self.systemtime = time.strftime("%H:%M:%S")
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


        #line edit
        self.input_number_of_people = QLineEdit()
        self.input_number_of_people.setMaximumSize(sizehint)


        #dates and times

        
        
        

        #add labels to layout
        self.add_customer_layout.addWidget(self.table_number_label,0,0)
        self.add_customer_layout.addWidget(self.display_table_number,0,1)
        

        self.add_customer_layout.addWidget(self.time_arrived_label,1,0)
        self.add_customer_layout.addWidget(self.date_arrived_label,2,0)

        self.add_customer_layout.addWidget(self.system_time_label,1,1)
        self.add_customer_layout.addWidget(self.system_date_label,2,1)

        self.add_customer_layout.addWidget(self.number_of_people_label,3,0)

        #add line edit to layout
        self.add_customer_layout.addWidget(self.input_number_of_people,3,1)


        #add button to layout
        self.create_complete_layout.addWidget(self.create_complete)
        
        #add layouts to main layout
        self.main_layout.addLayout(self.add_customer_layout)
        self.main_layout.addLayout(self.create_complete_layout)


        #create a widget to display main layout
        self.setLayout(self.main_layout)

        #connections
        self.create_complete.clicked.connect(self.create_booking)
        #self.exec_()

        
    
    def create_booking(self):
        TableNumber = self.display_table_number.text()

        #create bookingID for customer
        CustomerID = 1
        NumberOfPeople = self.input_number_of_people.text()
        Date = self.systemdate
        Time = self.systemtime
       

        Booking = (CustomerID,TableNumber,NumberOfPeople,Date,Time)
        print(Booking)

        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            sql = "insert into Bookings(CustomerID,TableNumber,NumberOfPeople,Date,Time) values (?,?,?,?,?)"
            cursor.execute(sql,Booking)
            db.commit()

        #get booking id and select * from bookings where bookingid = ?

        Time = ("{0}".format(Time))

        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Bookings where CustomerID = {0} and TableNumber = {1} and NumberOfPeople = {2} and Date = {3} and Time = {4} ".format(CustomerID,TableNumber,NumberOfPeople,Date,Time))
            bookingDetails = cursor.fetchone()
            print("Street booking : ".format(bookingDetails))
            return bookingDetails

        

        self.bookingCreated.emit()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = RandomCustomer(TableNumber)
    window.show()
    window.raise_()
    application.exec()
