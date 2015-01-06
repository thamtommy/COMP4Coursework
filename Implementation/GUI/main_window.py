#http://zetcode.com/gui/pyqt4/layoutmanagement/
#http://pyqt.sourceforge.net/Docs/PyQt4/qsqltablemodel.html#details <- display database

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
        #create toolbar
        self.example_tool_bar = QToolBar()
        self.test_tool_bar = QToolBar()

        self.example_label_bar = QPushButton("Example")
        self.example_label_bar.setToolTip("Hello this is an example")
        self.test_tool_label = QPushButton("Test")
        self.test_tool_label.setToolTip("This is a test")

        self.example_tool_bar.addWidget(self.example_label_bar)
        self.test_tool_bar.addWidget(self.test_tool_label)

        self.addToolBar(self.example_tool_bar)
        self.addToolBar(self.test_tool_bar)
        
        
        
        #create buttons
        #table buttons
        self.table_button = QPushButton("Table 1")
        self.table2_button = QPushButton("Table 2")
        self.table3_button = QPushButton("Table 3")
        self.table4_button = QPushButton("Table 4")
        self.table5_button = QPushButton("Table 5")
        self.table6_button = QPushButton("Table 6")
        self.table7_button = QPushButton("Table 7")
        self.table8_button = QPushButton("Table 8")
        self.table9_button = QPushButton("Table 9")
        self.table10_button = QPushButton("Table 10")
        self.table11_button = QPushButton("Table 11")
        self.table12_button = QPushButton("Table 12")
        self.table13_button = QPushButton("Table 13")
        self.table14_button = QPushButton("Table 14")
        self.table15_button = QPushButton("Table 15")
        self.table16_button = QPushButton("Table 16")

        self.manage_bookings = QPushButton("Manage Bookings") # Manage bookings button
        
        

        #labels
        self.test_label = QLabel("Test")
        self.booking_label = QLabel("Bookings")
        self.other_label = QLabel("Other")
        

        #create layouts
        self.main_layout = QGridLayout()
        self.table_layout = QGridLayout() #box 0,0
        self.booking_layout = QVBoxLayout() #box 1,0

        #add table buttons to table layout
        self.table_layout.addWidget(self.table_button,0,0)
        self.table_layout.addWidget(self.table2_button,0,1)
        self.table_layout.addWidget(self.table3_button,1,0)
        self.table_layout.addWidget(self.table4_button,1,1)
        self.table_layout.addWidget(self.table5_button,2,0)
        self.table_layout.addWidget(self.table6_button,2,1)
        self.table_layout.addWidget(self.table7_button,2,1)
        self.table_layout.addWidget(self.table8_button,2,1)
        self.table_layout.addWidget(self.table9_button,2,1)
        self.table_layout.addWidget(self.table10_button,3,0)
        self.table_layout.addWidget(self.table11_button,3,1)
        self.table_layout.addWidget(self.table12_button,4,0)
        self.table_layout.addWidget(self.table13_button,4,1)
        self.table_layout.addWidget(self.table14_button,5,0)
        self.table_layout.addWidget(self.table15_button,5,1)
        self.table_layout.addWidget(self.table16_button,6,0)
        #add button to booking layout
        self.booking_layout.addWidget(self.booking_label)
        self.booking_layout.addWidget(self.manage_bookings)
        

        #add layouts to main layout
        self.main_layout.addLayout(self.table_layout,0,0)
        #self.main_layout.addWidget(self.test_label,0,1) temporary
        self.main_layout.addLayout(self.booking_layout,1,0)
        #self.main_layout.addWidget(self.other_label,1,1)

        #create a widget to display main layout
        self.view_table_widget = QWidget()
        self.view_table_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.view_table_widget)

def main():
    restaurant_simulation = QApplication(sys.argv) # create new application
    restaurant_window = RestaurantWindow() #create new instance of main window
    restaurant_window.show() #make instance visible
    restaurant_window.raise_() #raise instance to top of window stack
    restaurant_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()
