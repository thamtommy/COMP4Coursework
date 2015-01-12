import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AddBookingWindow(QMainWindow):
    """this class creates a window to add bookings"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Booking")
        self.create_add_booking_layout()
        self.setFixedSize(800,600)

    def create_tool_bar(self):
        #create toolbar
        self.main_screen_tool_bar = QToolBar()
        self.orders_tool_bar = QToolBar()
        self.bookings_tool_bar = QToolBar()

        self.main_screen_label_bar = QPushButton("Main Screen")
        self.main_screen_label_bar.setToolTip("This will direct you to main screen")
        self.orders_label_bar = QPushButton("Orders")
        self.orders_label_bar.setToolTip("All orders will be displayed")
        self.bookings_label_bar = QPushButton("Bookings")
        self.bookings_label_bar.setToolTip("All bookings will be displayed")

        self.main_screen_tool_bar.addWidget(self.main_screen_label_bar)
        self.orders_tool_bar.addWidget(self.orders_label_bar)
        self.bookings_tool_bar.addWidget(self.bookings_label_bar)
        

        self.addToolBar(self.main_screen_tool_bar)
        self.addToolBar(self.orders_tool_bar)
        self.addToolBar(self.bookings_tool_bar)

    def create_add_booking_layout(self):
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

        #line edit
        self.input_first_name = QLineEdit()
        self.input_first_name.setMaximumSize(300,30)

        self.input_last_name = QLineEdit()
        self.input_last_name.setMaximumSize(300,30)
               
        self.input_number_of_people = QLineEdit()
        self.input_number_of_people.setMaximumSize(300,30)

        self.input_telephone_number = QLineEdit()
        self.input_telephone_number.setMaximumSize(300,30)


        #dates and times
        self.date_edit = QDateEdit()
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

        #add line edit to layout
        self.add_booking_layout.addWidget(self.input_first_name,0,1)
        self.add_booking_layout.addWidget(self.input_last_name,1,1)
        self.add_booking_layout.addWidget(self.date_edit,2,1)
        self.add_booking_layout.addWidget(self.time_edit,3,1)
        self.add_booking_layout.addWidget(self.input_number_of_people,4,1)
        self.add_booking_layout.addWidget(self.input_telephone_number,5,1)

        #add button to layout
        self.add_complete_layout.addWidget(self.add_complete)
        
        #add layouts to main layout
        self.main_layout.addLayout(self.add_booking_layout)
        self.main_layout.addLayout(self.add_complete_layout)


        #create a widget to display main layout
        self.add_booking_widget = QWidget()
        self.add_booking_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.add_booking_widget)

        #connections
        self.add_complete.clicked.connect(self.add_booking)

    def add_booking(self):
        FirstName = self.input_first_name.text()
        LastName = self.input_last_name.text()
        BookingDate = self.date_edit.text()
        BookingTime = self.time_edit.text()
        TeleNumber = self.input_telephone_number.text()
        booking = (FirstName,LastName,TeleNumber,BookingTime,BookingDate)
        print(booking)
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            sql = "insert into Booking(FirstName,LastName,TelephoneNo,BookingTime,BookingDate) values (?,?,?,?,?)"
            cursor.execute(sql,booking)
            db.commit()
            
                             

def main():
    restaurant_simulation = QApplication(sys.argv) # create new application
    restaurant_window = AddBookingWindow() #create new instance of main window
    restaurant_window.show() #make instance visible
    restaurant_window.raise_() #raise instance to top of window stack
    restaurant_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()

