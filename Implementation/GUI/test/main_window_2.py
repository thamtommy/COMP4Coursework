import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from manage_booking_test import *
#layout index
## 0 - main screen
## 1 - manage booking

from radio_button_widget_class import *

class RestaurantWindow(QMainWindow):
    """this class creates a main window to observe the restaurant"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restaurant Simulation")
        self.create_view_restaurant_layout()
          
        
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.main_widget_layout)
 
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        self.create_tool_bar()
        

        self.setFixedSize(1280,800)

        #layouts
        self.manage_booking = BookingWindow()
        self.stacked_layout.addWidget(self.manage_booking)

    def main_screen(self):
        self.stacked_layout.setCurrentIndex(0)
        
    def manage_booking(self):
        self.stacked_layout.setCurrentIndex(1)
        

    def create_tool_bar(self):
        #create toolbar
        self.main_screen_tool_bar = QToolBar()
        self.orders_tool_bar = QToolBar()        
        self.bookings_tool_bar = QToolBar()


        self.main_screen_label_bar = QPushButton("Main Screen")
        self.main_screen_label_bar.setToolTip("This will direct you to main screen")
        self.main_screen_label_bar.clicked.connect(self.main_screen)

        
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

    def create_menu_bar(self):
        self.menu = QMenuBar()
        self.menu_bar = self.menu.addMenu("Menu")
        self.options_bar = self.menu.addMenu("Options")
        self.setMenuBar(self.menu)



        
        
    

    def create_view_restaurant_layout(self):
        #methods
           
        self.create_menu_bar()
        
        #create buttons
        #table buttons
        self.table_button = QPushButton("Table 1")
        self.table_button.setGeometry(4,8,5,9)
        
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

        self.table_button.setMaximumSize(100,60)
        self.table2_button.setMaximumSize(100,60)
        self.table3_button.setMaximumSize(100,60)
        self.table4_button.setMaximumSize(100,60)
        self.table5_button.setMaximumSize(100,60)
        self.table6_button.setMaximumSize(100,60)
        self.table7_button.setMaximumSize(100,60)
        self.table8_button.setMaximumSize(100,60)
        self.table9_button.setMaximumSize(100,60)
        self.table10_button.setMaximumSize(100,60)
        self.table11_button.setMaximumSize(100,60)
        self.table12_button.setMaximumSize(100,60)
        self.table13_button.setMaximumSize(100,60)
        self.table14_button.setMaximumSize(100,60)
        self.table15_button.setMaximumSize(100,60)
        self.table16_button.setMaximumSize(100,60)

        
        #connections
        self.manage_bookings = QPushButton("Manage Bookings") # Manage bookings button
        self.manage_bookings.clicked.connect(self.manage_booking)
        
        

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
        self.table_layout.addWidget(self.table7_button,3,0)
        self.table_layout.addWidget(self.table8_button,3,1)
        self.table_layout.addWidget(self.table9_button,4,0)
        self.table_layout.addWidget(self.table10_button,4,1)
        self.table_layout.addWidget(self.table11_button,5,0)
        self.table_layout.addWidget(self.table12_button,5,1)
        self.table_layout.addWidget(self.table13_button,6,0)
        self.table_layout.addWidget(self.table14_button,6,1)
        self.table_layout.addWidget(self.table15_button,7,0)
        self.table_layout.addWidget(self.table16_button,7,1)
        #add button to booking layout
        self.booking_layout.addWidget(self.booking_label)
        self.booking_layout.addWidget(self.manage_bookings)
        

        #add layouts to main layout
        self.main_layout.addLayout(self.table_layout,0,0)
        #self.main_layout.addWidget(self.test_label,0,1) temporary
        self.main_layout.addLayout(self.booking_layout,1,0)
        #self.main_layout.addWidget(self.other_label,1,1)

        #create a widget to display main layout
        self.main_widget_layout = QWidget()
        self.main_widget_layout.setLayout(self.main_layout)




def main():
    restaurant_simulation = QApplication(sys.argv) # create new application
    restaurant_window = RestaurantWindow() #create new instance of main window
    restaurant_window.show() #make instance visible
    restaurant_window.raise_() #raise instance to top of window stack
    restaurant_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()

