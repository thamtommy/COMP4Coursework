import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AddBookingWindow(QWidget):
    bookingAdded = pyqtSignal()
    """this class creates a window to add bookings"""

    def __init__(self):
        super().__init__()

        #methods

        #create layouts
        self.main_layout = QVBoxLayout()
        self.add_booking_layout = QGridLayout()
        self.add_complete_layout = QHBoxLayout()
        
        
        #create buttons
        self.add_complete = QPushButton("Add Booking")
        
        #labels
        self.first_name_label = QLabel("First Name:")#Sometimes only first/last is given
        self.last_name_label = QLabel("Last Name:")
        self.date_label = QLabel("Date:")
        self.time_label = QLabel("Time:")
        self.number_of_people = QLabel("Number Of People:")
        self.telephone_number = QLabel("Telephone Number:")
        self.table_number_label = QLabel("Table Number:")

        #line edit
        self.input_first_name = QLineEdit()
        self.input_first_name.setMaximumSize(300,30)

        self.input_last_name = QLineEdit()
        self.input_last_name.setMaximumSize(300,30)
               
        self.input_number_of_people = QLineEdit()
        self.input_number_of_people.setMaximumSize(300,30)

        self.input_telephone_number = QLineEdit()
        self.input_telephone_number.setMaximumSize(300,30)
        self.input_telephone_number.setMaxLength(12)

        self.input_table_number = QLineEdit()       # drop down box
        self.input_table_number.setMaximumSize(300,30)


        #dates and times
        self.date_edit = QDateEdit()
        self.maximumdate = QDate(2050,1,30)
        self.date_edit.setMaximumDate(self.maximumdate)
        self.time_edit = QTimeEdit()
        
        
        
        #place holder text
        self.input_first_name.setPlaceholderText("First name given")
        self.input_last_name.setPlaceholderText("Last name given")
        self.input_number_of_people.setPlaceholderText("Expected number")
        self.input_telephone_number.setPlaceholderText("Telephone number given")

        #add labels to layout
        self.add_booking_layout.addWidget(self.first_name_label,0,0)
        self.add_booking_layout.addWidget(self.last_name_label,1,0)
        self.add_booking_layout.addWidget(self.date_label,2,0)
        self.add_booking_layout.addWidget(self.time_label,3,0)
        self.add_booking_layout.addWidget(self.number_of_people,4,0)
        self.add_booking_layout.addWidget(self.telephone_number,5,0)
        self.add_booking_layout.addWidget(self.table_number_label,6,0)

        #add line edit to layout
        self.add_booking_layout.addWidget(self.input_first_name,0,1)
        self.add_booking_layout.addWidget(self.input_last_name,1,1)
        self.add_booking_layout.addWidget(self.date_edit,2,1)
        self.add_booking_layout.addWidget(self.time_edit,3,1)
        self.add_booking_layout.addWidget(self.input_number_of_people,4,1)
        self.add_booking_layout.addWidget(self.input_telephone_number,5,1)
        self.add_booking_layout.addWidget(self.input_table_number,6,1)

        #add button to layout
        self.add_complete_layout.addWidget(self.add_complete)
        
        #add layouts to main layout
        self.main_layout.addLayout(self.add_booking_layout)
        self.main_layout.addLayout(self.add_complete_layout)


        #create a widget to display main layout
        self.add_booking_widget = QWidget()
        self.setLayout(self.main_layout)

        #connections
        self.add_complete.clicked.connect(self.add_booking)

    def add_booking(self):
        FirstName = self.input_first_name.text()
        LastName = self.input_last_name.text()
        TeleNumber = self.input_telephone_number.text()
        TableNumber = self.input_table_number.text()
        NumberOfPeople = self.input_number_of_people.text()
        TableNumber = int(TableNumber)
        NumberOfPeople = int(NumberOfPeople)

        
        BookingDate = self.date_edit.text()
        BookingTime = self.time_edit.text()


        customer = (FirstName,LastName,TeleNumber)

        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            sql = "insert into Customers(FirstName,LastName,TelephoneNo) values (?,?,?)"
            cursor.execute(sql,customer)
            db.commit()

        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("select CustomerID from Customers where TelephoneNo=?",(TeleNumber,))
            customerid = cursor.fetchone()[0]
            print(customerid)      
            
        booking = (customerid,TableNumber,NumberOfPeople,BookingDate,BookingTime)
        print(booking)
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            sql = "insert into Bookings(CustomerID,TableNumber,NumberOfPeople,Date,Time) values (?,?,?,?,?)"
            cursor.execute(sql,booking)
            db.commit()

        self.bookingAdded.emit()
            
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = AddBookingWindow()
    window.show()
    window.raise_()
    application.exec()
                             

