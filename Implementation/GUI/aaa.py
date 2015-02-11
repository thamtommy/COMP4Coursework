
# plan #
#get customers that booked to (table number), get booking details, get booking id so that I can use table BookingItems
#to manage order - display booking items table to track what customer ordered
#but first i need to get table number and pass it to methods


import sys
import time

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from manage_booking import *
from manage_order import *

from add_item_to_menu import *
from add_booking import *

from delete_item_off_menu import *
from delete_booking import*

from table_display import *
from table_class import *

from update_item_price import *


from off_the_street_booking import *
#from assign_table_customer import *



#stacked layout index
## 0 - main screen
## 1 - add item (menu bar)
## 2 - delete item (menu bar)
## 3 - view customers (tool bar)
## 4 - view bookings (tool bar)
## 5 - manage bookings (QPushButton)
## 6 - update item (menu bar)
## 7 - add booking (manage booking)
## 8 - delete booking (manage booking)
## 9 - street customer (tables)
## 10 - view dishes(tool bar)
## 11 - view dishes(tool bar)

class RestaurantWindow(QMainWindow):
    """this class creates a main window to observe the restaurant"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restaurant Simulation")
        self.TableNumber = None

        self.TableOneOccupied = False
        self.TableTwoOccupied = False
        self.TableThreeOccupied = False
        self.TableFourOccupied = False
        self.TableFiveOccupied = False
        self.TableSixOccupied = False
        self.TableSevenOccupied = False


        self.titleFont = QFont()
        self.titleFont.setPointSize(20)
        self.titleFont.setBold(True)
        
        self.create_menu_bar()
        self.create_tool_bar()
        
        self.main_stack_layout()
        #stacked layouts 
        self.stacked_layout = QStackedLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        self.stacked_layout.addWidget(self.main_widget_layout)
        self.add_item_stack_layout()
        self.delete_item_stack_layout()
        self.view_customers_stack_layout()
        self.view_bookings_stack_layout()
        self.manage_booking_stack_layout()
        self.update_item_stack_layout()
        self.add_booking_stack_layout()
        self.delete_booking_stack_layout()
        self.street_customer_stack_layout()
        self.view_dishes_stack_layout()
        self.view_drinks_stack_layout()

        


        
        self.setFixedSize(1280,860)


    def table_one(self):
        # the method street_customer_stack_layout is adding the widget holding the variable self.TableNumber which i assigned to None
        #which is why  TableNumber is always None
        
        self.TableNumber = 1

        if self.TableOneOccupied == False:
           #self.TableOne = Table()
            #self.TableOne.get_table_number(1)
            #TableNumber = self.TableOne._table_number
            self.street_customer = InitialiseCustomer(self.TableNumber)

            #self.street_customer.create_booking(TableNumber)

            self.street_customer_connect()
            
            self.TableOneOccupied = True
            print("Now occupied")
        else:
            print("Already occupied")
        
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Bookings where TableNumber = 1")
            bookings = cursor.fetchall()
            
            #print(bookings)

    def street_customer_stack_layout(self):
        self.TableNumber = 789
        self.street_customer = InitialiseCustomer(self.TableNumber)
        self.stacked_layout.addWidget(self.street_customer)

    def street_customer_connect(self):
        self.stacked_layout.setCurrentIndex(9)
    

    def table_two(self):
        if self.tableOccupied == False:
            self.tableOccupied = True
            print("Table 2 is now occupied")

        else:
            print("Table 2 is already occupied")

        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Bookings where TableNumber = 2")
            bookings = cursor.fetchall()
            print(bookings)
    
        

    def create_tool_bar(self):
        #create toolbar
        self.main_screen_tool_bar = QToolBar()
        self.orders_tool_bar = QToolBar()        
        self.bookings_tool_bar = QToolBar()
        self.view_customers = QToolBar()
        self.view_dishes = QToolBar()
        self.view_drinks = QToolBar()


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
        self.bookings_label_bar.triggered.connect(self.view_bookings_connect)

        self.view_customers_label = QAction("View Customer",self)
        self.view_customers_label.setToolTip("All customers will be displayed")
        self.view_customers.addAction(self.view_customers_label)
        self.view_customers_label.triggered.connect(self.view_customers_connect)
        
        self.view_dishes_label = QAction("View Dishes",self)
        self.view_dishes_label.setToolTip("All dishes will be displayed")
        self.view_dishes.addAction(self.view_dishes_label)
        self.view_dishes_label.triggered.connect(self.view_dishes_connect)
        
        self.view_drinks_label = QAction("View Drinks",self)
        self.view_drinks_label.setToolTip("All drinks will be displayed")
        self.view_drinks.addAction(self.view_drinks_label)
        self.view_drinks_label.triggered.connect(self.view_drinks_connect)

        self.addToolBar(self.main_screen_tool_bar)
        self.addToolBar(self.orders_tool_bar)
        self.addToolBar(self.bookings_tool_bar)
        self.addToolBar(self.view_customers)
        self.addToolBar(self.view_dishes)
        self.addToolBar(self.view_drinks)

    def create_menu_bar(self):
        #actions
        self.add_item_box = QAction("Add Item",self)
        self.delete_item_box = QAction("Delete Item",self)
        self.update_item_box = QAction("Update Item Price",self)
        
        self.menu = QMenuBar()
        self.menu_bar = self.menu.addMenu("Item Menu")
        self.options_bar = self.menu.addMenu("Options")
        self.setMenuBar(self.menu)

        self.menu_bar.addAction(self.add_item_box)
        self.menu_bar.addAction(self.delete_item_box)
        self.menu_bar.addAction(self.update_item_box)
        
        #connections
        self.add_item_box.triggered.connect(self.add_item_menu_connect)
        self.delete_item_box.triggered.connect(self.delete_item_menu_connect)
        self.update_item_box.triggered.connect(self.update_item_connect)

    def main_stack_layout(self):

        #create layouts
        self.main_layout = QVBoxLayout()
        self.table_layout = QGridLayout() #box 0,0
        self.booking_layout = QVBoxLayout() #box 1,0
        self.table_layout.setColumnStretch(0,5)
        
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

        self.table_button.setMaximumSize(250,60)
        self.table2_button.setMaximumSize(200,60)
        self.table3_button.setMaximumSize(200,60)
        self.table4_button.setMaximumSize(200,60)
        self.table5_button.setMaximumSize(200,60)
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


        #booking section

        self.manage_bookings = QPushButton("Manage Bookings") # Manage bookings button
        TodaysDate = time.strftime("%d/%m/%Y")
        print(TodaysDate)
        
        filter_query = "Date like '%{0}%'".format(TodaysDate)
        #if not hasattr(self,"display_widget"):
        self.display_bookings = DisplayTable()
        self.display_bookings.show_table("Bookings")
        self.display_bookings.model.setFilter(filter_query)
        


        
        #connections
        self.table_button.clicked.connect(self.table_one)
        self.table2_button.clicked.connect(self.table_two)

        self.manage_bookings.clicked.connect(self.manage_booking_connect)

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


        #add widgets to booking layout
        self.todays_bookings_label = QLabel("Todays Bookings")
        self.todays_bookings_label.setFont(self.titleFont)
        self.todays_bookings_label.setFixedWidth(400)
        
        self.booking_layout.addWidget(self.todays_bookings_label)
        self.booking_layout.addWidget(self.display_bookings)
        self.booking_layout.addWidget(self.manage_bookings)
        
        

        #add layouts to main layout
        self.main_layout.addLayout(self.table_layout)
        self.main_layout.addLayout(self.booking_layout)


        #create a widget to display main layout
        self.main_widget_layout = QWidget()
        self.main_widget_layout.setLayout(self.main_layout)

        return self.main_widget_layout
    
    def add_item_stack_layout(self):
        self.add_menu_item = AddItemToMenu()

        if not hasattr(self,"add_item_menu_bar"):
            self.add_item_menu_bar = DisplayTable()
        self.add_item_menu_bar.show_table("Items")

        self.add_item_layout = QVBoxLayout()
        self.add_item_layout.addWidget(self.add_item_menu_bar)
        self.add_item_layout.addWidget(self.add_menu_item)
        self.add_item_widget = QWidget()
        self.add_item_widget.setLayout(self.add_item_layout)
        self.stacked_layout.addWidget(self.add_item_widget)
        self.add_menu_item.itemAdded.connect(self.add_item_menu_bar.refresh)
             

    def add_item_menu_connect(self):
        self.stacked_layout.setCurrentIndex(1)


    def delete_item_stack_layout(self):
        self.delete_menu_item = DeleteItemOffMenu()
        if not hasattr(self,"display_widget2"):
            self.display_widget2 = DisplayTable()
        self.display_widget2.show_table("Items")

        self.delete_item_layout = QVBoxLayout()
        self.delete_item_layout.addWidget(self.display_widget2)
        self.delete_item_layout.addWidget(self.delete_menu_item)
        self.delete_item_widget = QWidget()
        self.delete_item_widget.setLayout(self.delete_item_layout)
        self.stacked_layout.addWidget(self.delete_item_widget)
        self.delete_menu_item.itemDeleted.connect(self.display_widget2.refresh) 
    

    def delete_item_menu_connect(self):
        self.stacked_layout.setCurrentIndex(2)

    def view_customers_stack_layout(self):
        self.display_widget2 = DisplayTable()
        self.display_widget2.show_table("Customers")

        self.view_customers_layout = QVBoxLayout()
        self.view_customers_layout.addWidget(self.display_widget2)
        self.view_customers_widget = QWidget()
        self.view_customers_widget.setLayout(self.view_customers_layout)
        self.stacked_layout.addWidget(self.view_customers_widget)

    def view_customers_connect(self):
        self.stacked_layout.setCurrentIndex(3)

    def view_bookings_stack_layout(self):
        #if not hasattr(self,"display_widget"):
        self.tool_bar_bookings = DisplayTable()
        self.tool_bar_bookings.show_table("Bookings")

        self.view_bookings_layout = QVBoxLayout()
        self.view_bookings_layout.addWidget(self.tool_bar_bookings)
        self.view_bookings_widget = QWidget()
        self.view_bookings_widget.setLayout(self.view_bookings_layout)
        self.stacked_layout.addWidget(self.view_bookings_widget) 

    def view_bookings_connect(self):
        self.stacked_layout.setCurrentIndex(4)

    def main_screen(self):
        self.stacked_layout.setCurrentIndex(0)
        
    def manage_booking_stack_layout(self):
        self.manage_bookings = BookingWindow()
        self.manage_bookings.add_button.clicked.connect(self.add_booking_connect) #connection
        self.manage_bookings.delete_button.clicked.connect(self.delete_booking_connect) #connection

        #if not hasattr(self,"display_widget"):
        self.display_booking_table = DisplayTable()
        self.display_booking_table.show_table("Bookings")

        self.manage_booking_layout = QVBoxLayout()
        self.manage_booking_layout.addWidget(self.display_booking_table)
        self.manage_booking_layout.addWidget(self.manage_bookings)
        self.manage_booking_widget = QWidget()
        self.manage_booking_widget.setLayout(self.manage_booking_layout)
        self.stacked_layout.addWidget(self.manage_booking_widget)

    def manage_booking_connect(self):
        self.stacked_layout.setCurrentIndex(5)
    
    def update_item_stack_layout(self):
        self.update_item = UpdateItemPrice()

        #if not hasattr(self,"display_widget"):
        self.update_price_menu = DisplayTable()
        self.update_price_menu.show_table("Items")

        self.update_item_layout = QVBoxLayout()
        self.update_item_layout.addWidget(self.update_price_menu)
        self.update_item_layout.addWidget(self.update_item)
        self.update_item_widget = QWidget()
        self.update_item_widget.setLayout(self.update_item_layout)
        self.stacked_layout.addWidget(self.update_item_widget)
        self.update_item.itemPriceUpdated.connect(self.update_price_menu.refresh)
        

    def update_item_connect(self):
        self.stacked_layout.setCurrentIndex(6)

    def add_booking_stack_layout(self):
        self.add_booking = AddBookingWindow()
       
        self.booking_table_widget = DisplayTable()
        self.booking_table_widget.show_table("Bookings")

        self.add_booking_layout = QVBoxLayout()
        self.add_booking_layout.addWidget(self.booking_table_widget)
        self.add_booking_layout.addWidget(self.add_booking)
        self.add_booking_widget = QWidget()
        self.add_booking_widget.setLayout(self.add_booking_layout)
        self.stacked_layout.addWidget(self.add_booking_widget)
        self.add_booking.bookingAdded.connect(self.booking_table_widget.refresh)
        

    def add_booking_connect(self):
        self.stacked_layout.setCurrentIndex(7)


    def delete_booking_stack_layout(self):
        self.delete_booking = DeleteBookingWindow()
        self.booking_table_widget2 = DisplayTable()
        self.booking_table_widget2.show_table("Bookings")

        self.delete_booking_layout = QVBoxLayout()
        self.delete_booking_layout.addWidget(self.booking_table_widget2)
        self.delete_booking_layout.addWidget(self.delete_booking)
        self.delete_booking_widget = QWidget()
        self.delete_booking_widget.setLayout(self.delete_booking_layout)
        self.stacked_layout.addWidget(self.delete_booking_widget)
        self.delete_booking.bookingDeleted.connect(self.booking_table_widget2.refresh)

    def delete_booking_connect(self):
        self.stacked_layout.setCurrentIndex(8)

    def view_dishes_stack_layout(self):
        filter_query = "ItemTypeID like '%1%'"

        #if not hasattr(self,"display_widget"):
        self.view_dishes_tool = DisplayTable()
        self.view_dishes_tool.show_table("Items")
        self.view_dishes_tool.model.setFilter(filter_query)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.view_dishes_tool)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.stacked_layout.addWidget(self.main_widget) 
      

    def view_dishes_connect(self):
        self.stacked_layout.setCurrentIndex(10)

    def view_drinks_stack_layout(self):
        filter_query = "ItemTypeID like '%2%'"

        #if not hasattr(self,"display_widget"):
        self.view_drinks_tool = DisplayTable()
        self.view_drinks_tool.show_table("Items")
        self.view_drinks_tool.model.setFilter(filter_query)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.view_drinks_tool)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.stacked_layout.addWidget(self.main_widget) 
     

    def view_drinks_connect(self):
        self.stacked_layout.setCurrentIndex(11)


def main():
    restaurant_simulation = QApplication(sys.argv) # create new application
    restaurant_window = RestaurantWindow() #create new instance of main window
    restaurant_window.show() #make instance visible
    restaurant_window.raise_() #raise instance to top of window stack
    restaurant_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()

