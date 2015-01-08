import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button_widget_class import *

class AddBookingWindow(QMainWindow):
    """this class creates a main window to observe the restaurant"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Booking")
        self.create_add_booking_layout()

    def create_add_booking_layout(self):
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

        #create layouts
        self.main_layout = QVBoxLayout()
        self.add_booking_layout = QGridLayout()        
        
        
        #create buttons
        self.add_complete = QPushButton("Add Booking")
        
        #labels
        self.name_label = QLabel("Name")
        self.date_label = QLabel("Date")
        self.time_label = QLabel("Time")
        self.number_of_people = QLabel("Number of people")

        #line edit
        self.input_name = QLineEdit()
        self.input_date = QLineEdit()
        self.input_time = QLineEdit()
        self.input_number_of_people = QLineEdit()
        


        
        #place holder text
        self.input_name.setPlaceholderText("Add Name")

        #add labels to layout
        self.add_booking_layout.addWidget(self.name_label,0,0)
        self.add_booking_layout.addWidget(self.date_label,1,0)
        self.add_booking_layout.addWidget(self.time_label,2,0)
        self.add_booking_layout.addWidget(self.number_of_people,3,0)

        #add line edit to layout
        self.add_booking_layout.addWidget(self.input_name,0,1)
        self.add_booking_layout.addWidget(self.input_date,1,1)
        self.add_booking_layout.addWidget(self.input_time,2,1)
        self.add_booking_layout.addWidget(self.input_number_of_people,3,1)
        
        #add layouts to main layout
        self.main_layout.addLayout(self.add_booking_layout)


        #create a widget to display main layout
        self.view_table_widget = QWidget()
        self.view_table_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.view_table_widget)

def main():
    restaurant_simulation = QApplication(sys.argv) # create new application
    restaurant_window = AddBookingWindow() #create new instance of main window
    restaurant_window.show() #make instance visible
    restaurant_window.raise_() #raise instance to top of window stack
    restaurant_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()

