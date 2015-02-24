import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from table_display import *
import time

class UpdateBooking(QWidget):
    bookingAdded = pyqtSignal()
    """this class is used to update bookings"""

    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()
        self.update_booking_layout = QGridLayout()
        
        self.display_table = DisplayTable()
        self.display_table.show_table("Bookings")
        
        self.date_button = QPushButton("Update Date")
        self.time_button = QPushButton("Update Time")
        self.people_button = QPushButton("Update Number Of People")
        self.table_button = QPushButton("Update Table")
        self.telenumber_button = QPushButton("Update TeleNumber")

        self.bookingID_label = QLabel("Booking ID you want to update: ")
        self.date_label = QLabel("Date:")
        self.time_label = QLabel("Time:")
        self.number_of_people = QLabel("Number Of People:")
        self.telephone_number = QLabel("Telephone Number:")
        self.table_number_label = QLabel("Table Number:")

        self.input_bookingID = QLineEdit()
        self.input_bookingID.setMaximumSize(300,30)
        self.input_number_of_people = QLineEdit()
        regexp = QRegExp("^\d\d")
        validator = QRegExpValidator(regexp)
        self.input_number_of_people.setValidator(validator)
        self.input_number_of_people.setMaximumSize(300,30)
        self.input_number_of_people.setMaxLength(2)
        self.input_number_of_people.setPlaceholderText("Expected number")


        self.select_table_number = QComboBox(self)
        self.select_table_number.setMaximumSize(300,30)
        for each in range(1,17):
            self.select_table_number.addItem(str(each))

        #dates and times
        self.date_edit = QDateEdit()
        self.maximumdate = QDate(2050,1,30)
        self.minimumdate = QDate(2015,1,1)
        self.date_edit.setMaximumDate(self.maximumdate)
        self.date_edit.setMinimumDate(self.minimumdate)
        self.date_edit.setMaximumSize(300,30)
        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("hh:mm")
        self.time_edit.setMaximumSize(300,30)
        
        
        self.update_booking_layout.addWidget(self.bookingID_label,0,0)
        self.update_booking_layout.addWidget(self.date_label,1,0)
        self.update_booking_layout.addWidget(self.time_label,2,0)
        self.update_booking_layout.addWidget(self.number_of_people,3,0)
        self.update_booking_layout.addWidget(self.table_number_label,4,0)

        self.update_booking_layout.addWidget(self.input_bookingID,0,1)
        self.update_booking_layout.addWidget(self.date_edit,1,1)
        self.update_booking_layout.addWidget(self.time_edit,2,1)
        self.update_booking_layout.addWidget(self.input_number_of_people,3,1)
        self.update_booking_layout.addWidget(self.select_table_number,4,1)

        self.update_booking_layout.addWidget(self.date_button,1,2)
        self.update_booking_layout.addWidget(self.time_button,2,2)
        self.update_booking_layout.addWidget(self.people_button,3,2)
        self.update_booking_layout.addWidget(self.table_button,4,2)
        
        #add layouts to main layout
        self.main_layout.addWidget(self.display_table)
        self.main_layout.addLayout(self.update_booking_layout)


        #create a widget to display main layout
        self.setLayout(self.main_layout)
        

        
        #connections
        self.date_button.clicked.connect(self.update_date)
        self.time_button.clicked.connect(self.update_time)
        self.people_button.clicked.connect(self.update_peopleNo)
        self.table_button.clicked.connect(self.update_tableNo)
        

    def update_date(self): 
        bookingID = self.input_bookingID.text()
        BookingDate = self.date_edit.text()
        UpdateDate = (BookingDate,bookingID)
        
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            sql = "update Bookings set Date=? where BookingID=?"
            cursor.execute(sql,UpdateDate)
            db.commit()

        self.display_table.refresh()

    def update_time(self):
        bookingID = self.input_bookingID.text()
        BookingTime = self.time_edit.text()
        UpdateTime = (BookingTime,bookingID)
        
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            sql = "update Bookings set Time=? where BookingID=?"
            cursor.execute(sql,UpdateTime)
            db.commit()

        self.display_table.refresh()


    def update_peopleNo(self):
        bookingID = self.input_bookingID.text()
        NumberOfPeople = int(self.input_number_of_people.text())
        UpdatePeople = (NumberOfPeople,bookingID)
        if len(str(NumberOfPeople)) > 0:
             with sqlite3.connect("restaurant.db") as db:
                cursor = db.cursor()
                sql = "update Bookings set NumberOfPeople=? where BookingID=?"
                cursor.execute(sql,UpdatePeople)
                db.commit()

             self.display_table.refresh()
        else:
            print("Please enter a value")


    def update_tableNo(self):
        bookingID = self.input_bookingID.text()
        TableNumber = self.select_table_number.currentIndex() + 1 
        UpdateTableNo = (TableNumber,bookingID)
        
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            sql = "update Bookings set TableNumber=? where BookingID=?"
            cursor.execute(sql,UpdateTableNo)
            db.commit()

        self.display_table.refresh()
        

        

            
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = UpdateBooking()
    window.show()
    window.raise_()
    application.exec()
                             

