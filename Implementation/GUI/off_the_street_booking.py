import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time

class InitialiseCustomer(QDialog):
    """this class creates a window to add bookings"""

    def __init__(self,TableNumber):
        super().__init__()

        #methods

        #create layouts
        self.main_layout = QVBoxLayout()
        self.add_customer_layout = QGridLayout()
        self.create_complete_layout = QHBoxLayout()
        
        
        #create buttons
        self.create_complete = QPushButton("Create")
        
        #labels
        self.number_of_people_label = QLabel("Number Of People : ")
        self.time_arrived_label = QLabel("Time Of Arrival : ")
        self.date_arrived_label = QLabel("Date Of Arrival : ")

        self.systemtime = time.strftime("%H:%M:%S")
        self.system_time_label = QLabel(self.systemtime)

        self.systemdate = time.strftime("%d/%m/%Y")
        self.system_date_label = QLabel(self.systemdate)


        #line edit
        self.input_number_of_people = QLineEdit()
        self.input_number_of_people.setMaximumSize(300,30)


        #dates and times

        
        
        

        #add labels to layout
        self.add_customer_layout.addWidget(self.number_of_people_label,0,0)
        self.add_customer_layout.addWidget(self.time_arrived_label,1,0)
        self.add_customer_layout.addWidget(self.date_arrived_label,2,0)

        self.add_customer_layout.addWidget(self.system_time_label,1,1)
        self.add_customer_layout.addWidget(self.system_date_label,2,1)

        #add line edit to layout
        self.add_customer_layout.addWidget(self.input_number_of_people,0,1)


        #add button to layout
        self.create_complete_layout.addWidget(self.create_complete)
        
        #add layouts to main layout
        self.main_layout.addLayout(self.add_customer_layout)
        self.main_layout.addLayout(self.create_complete_layout)


        #create a widget to display main layout
        self.setLayout(self.main_layout)

        #connections
        self.create_complete.clicked.connect(self.create_booking)

    def create_booking(self):
        #create orderID for customer
        TotalDrinkPrice = 0
        TotalDishPrice = 0
        TotalPrice = TotalDrinkPrice+TotalDishPrice

        Order = (TotalDrinkPrice,TotalDishPrice,TotalPrice)

        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            sql = "insert into Bookings(CustomerID,TableNumber,NumberOfPeople,Date,Time) values (?,?,?,?,?)"
            cursor.execute(sql,booking)
            db.commit()  

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = InitialiseCustomer()
    window.show()
    window.raise_()
    application.exec()
                             

