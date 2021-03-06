import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from table_display import *
import time

class AddBookingWindow(QWidget):

    """this class creates a widget to add bookings"""

    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()
        self.add_booking_layout = QGridLayout()
        self.add_complete_layout = QHBoxLayout()
        
        self.display_table = DisplayTable()
        self.display_table.show_table("Bookings")
        self.add_complete = QPushButton("Add Booking")
        
        self.first_name_label = QLabel("First Name:")
        self.last_name_label = QLabel("Last Name:")
        self.date_label = QLabel("Date:")
        self.time_label = QLabel("Time:")
        self.number_of_people = QLabel("Number Of People:")
        self.telephone_number = QLabel("Telephone Number:")
        self.table_number_label = QLabel("Table Number:")

        regExp = QRegExp("^[a-zA-Z]+$")
        Validator = QRegExpValidator(regExp)
        self.input_first_name = QLineEdit()
        self.input_first_name.setValidator(Validator)
        self.input_first_name.setMaximumSize(300,30)
        self.input_last_name = QLineEdit()
        self.input_last_name.setValidator(Validator)
        
        self.input_last_name.setMaximumSize(300,30)
               
        self.input_number_of_people = QLineEdit()
        regexp = QRegExp("^\d|\d\d")
        validator = QRegExpValidator(regexp)
        self.input_number_of_people.setValidator(validator)
        self.input_number_of_people.setMaximumSize(300,30)
        self.input_number_of_people.setMaxLength(2)

        regexp2 = QRegExp("^[0-9]*$")
        validator2 = QRegExpValidator(regexp2)

        self.input_telephone_number = QLineEdit()
        self.input_telephone_number.setValidator(validator2)
        self.input_telephone_number.setMaximumSize(300,30)
        self.input_telephone_number.setMaxLength(11)

        self.select_table_number = QComboBox(self)
        for each in range(1,17):
            self.select_table_number.addItem(str(each))


        #dates and times
        self.date_edit = QDateEdit()
        self.maximumdate = QDate(2050,1,30)
        self.minimumdate = QDate.currentDate()
        self.date_edit.setMaximumDate(self.maximumdate)
        self.date_edit.setMinimumDate(self.minimumdate)
        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("hh:mm")
        
        
        
        #place holder text
        self.input_first_name.setPlaceholderText("First name given")
        self.input_last_name.setPlaceholderText("Last name given")
        self.input_number_of_people.setPlaceholderText("Expected number")
        self.input_telephone_number.setPlaceholderText("Telephone number given")

        self.add_booking_layout.addWidget(self.first_name_label,0,0)
        self.add_booking_layout.addWidget(self.last_name_label,1,0)
        self.add_booking_layout.addWidget(self.date_label,2,0)
        self.add_booking_layout.addWidget(self.time_label,3,0)
        self.add_booking_layout.addWidget(self.number_of_people,4,0)
        self.add_booking_layout.addWidget(self.telephone_number,5,0)
        self.add_booking_layout.addWidget(self.table_number_label,6,0)

        self.add_booking_layout.addWidget(self.input_first_name,0,1)
        self.add_booking_layout.addWidget(self.input_last_name,1,1)
        self.add_booking_layout.addWidget(self.date_edit,2,1)
        self.add_booking_layout.addWidget(self.time_edit,3,1)
        self.add_booking_layout.addWidget(self.input_number_of_people,4,1)
        self.add_booking_layout.addWidget(self.input_telephone_number,5,1)
        self.add_booking_layout.addWidget(self.select_table_number,6,1)
        self.add_complete_layout.addWidget(self.add_complete)
        
        #add layouts to main layout
        self.main_layout.addWidget(self.display_table)
        self.main_layout.addLayout(self.add_booking_layout)
        self.main_layout.addLayout(self.add_complete_layout)
        self.setLayout(self.main_layout)
        

        #connections
        self.add_complete.clicked.connect(self.add_booking)

    def add_booking(self):
        FirstName = self.input_first_name.text().capitalize()
        LastName = self.input_last_name.text().capitalize()
        TeleNumber = self.input_telephone_number.text()
        try:
            NumberOfPeople = int(self.input_number_of_people.text())
        except ValueError:
            pass
        TableNumber = self.select_table_number.currentIndex() + 1  
        BookingDate = self.date_edit.text()
        BookingTime = self.time_edit.text()

        try:
        
            if (len(FirstName) > 1) and (len(LastName) > 1) and ((len(str(NumberOfPeople))) > 0 and (NumberOfPeople)>1) and (len(str(TeleNumber)) == 11): 

                customer = (FirstName,LastName,TeleNumber)

                with sqlite3.connect("restaurant.db") as db:
                    cursor = db.cursor()
                    sql = "insert into Customers(FirstName,LastName,TelephoneNo) values (?,?,?)"
                    cursor.execute(sql,customer)
                    db.commit()

                with sqlite3.connect("restaurant.db") as db:
                    cursor = db.cursor()
                    cursor.execute("select CustomerID from Customers where TelephoneNo=? and FirstName=? and LastName=?",(TeleNumber,FirstName,LastName))
                    customerid = cursor.fetchone()[0]
                    print(customerid)      
                    
                booking = (customerid,TableNumber,NumberOfPeople,BookingDate,BookingTime)
                print(booking)
                with sqlite3.connect("restaurant.db") as db:
                    cursor = db.cursor()
                    sql = "insert into Bookings(CustomerID,TableNumber,NumberOfPeople,Date,Time) values (?,?,?,?,?)"
                    cursor.execute("PRAGMA foreign_keys = ON")
                    cursor.execute(sql,booking)
                    db.commit()

                self.display_table.refresh()
            else:
                QMessageBox.about(self, "Error","Please make sure you haven't left any empty spaces")

        except ValueError:
            print("Booking unsucessful")
            
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = AddBookingWindow()
    window.show()
    window.raise_()
    application.exec()
                             

