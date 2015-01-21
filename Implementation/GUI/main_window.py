import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from manage_booking import *
from manage_order import *
from add_item_to_menu import *
from delete_item_off_menu import *
from table_display import *


#layout index
## 0 - main screen
## 1 - manage booking

from radio_button_widget_class import *

class RestaurantWindow(QMainWindow):
    """this class creates a main window to observe the restaurant"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restaurant Simulation")
        self.create_menu_bar()
        
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

        self.main_layout.addLayout(self.booking_layout,1,0)


        #create a widget to display main layout
        self.main_widget_layout = QWidget()
        self.main_widget_layout.setLayout(self.main_layout)
          
        
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.main_widget_layout)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        self.create_tool_bar()

        

        self.setFixedSize(1280,800)

        #layouts
    def main_screen(self):
        self.stacked_layout.setCurrentIndex(0)
        
    def manage_booking(self):
        self.manage_bookings = BookingWindow()
        self.display_widget = DisplayTable()
        self.display_widget.show_table("Booking")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display_widget)
        self.layout.addWidget(self.manage_bookings)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)
        
        

    def create_tool_bar(self):
        #create toolbar
        self.main_screen_tool_bar = QToolBar()
        self.orders_tool_bar = QToolBar()        
        self.bookings_tool_bar = QToolBar()
        self.view_customers = QToolBar()


        self.main_screen_label_bar = QAction("Main Screen",self)
        self.main_screen_label_bar.setToolTip("This will direct you to main screen")
        self.main_screen_tool_bar.addAction(self.main_screen_label_bar)
        self.main_screen_label_bar.triggered.connect(self.main_screen)
      
        self.orders_label_bar = QAction("Orders",self)
        self.orders_label_bar.setToolTip("All orders will be displayed")
        self.orders_tool_bar.addAction(self.orders_label_bar)

        self.bookings_label_bar = QAction("Bookings",self)
        self.bookings_label_bar.setToolTip("All bookings will be displayed")
        self.bookings_tool_bar.addAction(self.bookings_label_bar)

        self.view_customers_label = QAction("View Customer",self)
        self.view_customers_label.setToolTip("All customers will be displayed")
        self.view_customers.addAction(self.view_customers_label)
        self.view_customers_label.triggered.connect(self.view_customers_connection)
        

        

        self.addToolBar(self.main_screen_tool_bar)
        self.addToolBar(self.orders_tool_bar)
        self.addToolBar(self.bookings_tool_bar)
        self.addToolBar(self.view_customers)

    def create_menu_bar(self):
        #actions
        self.add_item_box = QAction("Add Item",self)
        self.delete_item_box = QAction("Delete Item",self)
        
        self.menu = QMenuBar()
        self.menu_bar = self.menu.addMenu("Menu")
        self.options_bar = self.menu.addMenu("Options")
        self.setMenuBar(self.menu)

        self.menu_bar.addAction(self.add_item_box)
        self.menu_bar.addAction(self.delete_item_box)      
        
        #connections
        self.add_item_box.triggered.connect(self.add_item_menu_connection)
        
        self.delete_item_box.triggered.connect(self.delete_item_menu_connection)
    
    def add_item_menu_connection(self):
        self.add_menu_item = AddItemToMenu()
        self.display_widget = DisplayTable()
        self.display_widget.show_table("Menu")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display_widget)
        self.layout.addWidget(self.add_menu_item)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)


    def delete_item_menu_connection(self):
        self.delete_menu_item = DeleteItemOffMenu()
        self.display_widget = DisplayTable()
        self.display_widget.show_table("Menu")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display_widget)
        self.layout.addWidget(self.delete_menu_item)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def view_customers_connection(self):
        self.display_widget = DisplayTable()
        self.display_widget.show_table("Customer")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display_widget)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)
        






def main():
    restaurant_simulation = QApplication(sys.argv) # create new application
    restaurant_window = RestaurantWindow() #create new instance of main window
    restaurant_window.show() #make instance visible
    restaurant_window.raise_() #raise instance to top of window stack
    restaurant_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()

