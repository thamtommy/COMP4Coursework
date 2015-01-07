#http://zetcode.com/gui/pyqt4/layoutmanagement/

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button_widget_class import *

class RestaurantWindow(QMainWindow):
    """this class creates a main window to observe the restaurant"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restaurant Simulation")
        self.create_view_restaurant_layout()

    def create_view_restaurant_layout(self):
        #create buttons
        self.table_button = QPushButton("Table 1")
        self.table2_button = QPushButton("Table 2")

        #labels
        self.test_label = QLabel("Test")
        self.booking_label = QLabel("Bookings")
        self.other_label = QLabel("Other")
        

        #create layouts
        self.main_layout = QGridLayout()
        self.table_layout = QGridLayout()

        #add table buttons to table layout
        self.table_layout.addWidget(self.table_button,0,0)
        self.table_layout.addWidget(self.table2_button,0,1)

        #add table layout to main layout at box 0,0
        self.main_layout.addLayout(self.table_layout,0,0)
        self.main_layout.addWidget(self.test_label,0,1)
        self.main_layout.addWidget(self.booking_label,1,0)
        self.main_layout.addWidget(self.other_label,1,1)

        #create a widget to display main layout
        self.view_table_widget = QWidget()
        self.view_table_widget.setLayout(self.main_layout)

def main():
    restaurant_simulation = QApplication(sys.argv) # create new application
    restaurant_window = RestaurantWindow() #create new instance of main window
    restaurant_window.show() #make instance visible
    restaurant_window.raise_() #raise instance to top of window stack
    restaurant_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()
