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

from update_item_price import *
from radio_button_widget_class import *


from off_the_street_booking import *
from assign_table_customer import *



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
## 9 - view dishes(tool bar)
## 10 - view dishes(tool bar)

class RestaurantWindow(QMainWindow):
    """this class creates a main window to observe the restaurant"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restaurant Simulation")

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
        self.view_dishes_stack_layout()
        self.view_drinks_stack_layout()
        

        


        
        self.setFixedSize(1280,860)          

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

        self.add_booking_box = QAction("Add Booking",self)
        self.delete_booking_box = QAction("Delete Booking",self)
        
        self.menu = QMenuBar()
        self.menu_bar = self.menu.addMenu("Item Menu")
        self.bookings_bar = self.menu.addMenu("Bookings")
        self.options_bar = self.menu.addMenu("Options")
        
        self.setMenuBar(self.menu)

        self.menu_bar.addAction(self.add_item_box)
        self.menu_bar.addAction(self.delete_item_box)
        self.menu_bar.addAction(self.update_item_box)

        self.bookings_bar.addAction(self.add_booking_box)
        self.bookings_bar.addAction(self.delete_booking_box)
        
        
        #connections
        self.add_item_box.triggered.connect(self.add_item_menu_connect)
        self.delete_item_box.triggered.connect(self.delete_item_menu_connect)
        self.update_item_box.triggered.connect(self.update_item_connect)

        self.add_booking_box.triggered.connect(self.add_booking_connect)
        self.delete_booking_box.triggered.connect(self.delete_booking_connect)

    def radio_button_connect(self):
        TableNumber = self.table_buttons.selected_button()
        print(TableNumber)
        if TableNumber == 1:
            if self.TableOneOccupied == False:
                self.table1 = AssignCustomer(TableNumber)
                bookingDetails = self.table1.bookingDetails
                self.TableOneOrder = OrderWindow(bookingDetails)
                self.TableOneOccupied = True
                if self.TableOneOrder.Finished == True:
                    self.TableOneOccupied = False
            elif self.TableOneOccupied == True:
                bookingDetails = self.table1.bookingDetails
                self.TableOneOrder = OrderWindow(bookingDetails)
                

                             
                
        elif TableNumber == 2:
            if self.TableTwoOccupied == False:
                self.table2 = AssignCustomer(TableNumber)
                self.table2.bookingRetrieved.connect(self.table2.close)
                bookingDetails = self.table2.bookingDetails
                self.TableTwoOrder = OrderWindow(bookingDetails)
                self.TableTwoOccupied = True
            elif self.TableTwoOccupied == True:
                bookingDetails = self.table2.bookingDetails
                self.TableTwoOrder = OrderWindow(bookingDetails)
                             


        elif TableNumber == 3:
            if self.TableThreeOccupied == False:
                self.table3 = AssignCustomer(TableNumber)
                self.table3.bookingRetrieved.connect(self.table3.close)
                bookingDetails = self.table3.bookingDetails
                self.TableThreeOrder = OrderWindow(bookingDetails)
                self.TableThreeOccupied = True
            elif self.TableThreeOccupied == True:
                bookingDetails = self.table3.bookingDetails
                self.TableThreeOrder = OrderWindow(bookingDetails)
                

    def main_stack_layout(self):

        #create layouts
        self.main_layout = QVBoxLayout()
        self.booking_layout = QVBoxLayout() #box 1,0
        self.table_radio_layout = QVBoxLayout()


        #radio button
        
        tableList = []
        for each in range(1,17):
            tableList.append("Table {0}".format(each))
            
        self.table_buttons = RadioButtonWidget("Table Numbers", "Please select a Table" , tableList)
        self.select_table_button = QPushButton("Select Table")
        self.select_table_button.clicked.connect(self.radio_button_connect)
        
        
        self.table_radio_layout.addWidget(self.table_buttons)
        self.table_radio_layout.addWidget(self.select_table_button)
        

        #booking section

        self.manage_bookings = QPushButton("Manage Bookings") # Manage bookings button
        TodaysDate = time.strftime("%d/%m/%Y")
        print(TodaysDate)

        bookingQuery = """SELECT
                        Customers.FirstName,
                        Customers.LastName,
                        Bookings.NumberOfPeople,
                        Bookings.TableNumber,
                        Bookings.Time
                        FROM Customers
                        INNER JOIN Bookings
                        ON Customers.CustomerID = Bookings.CustomerID
                        WHERE Bookings.Date = '{0}'
                        """.format(TodaysDate)
        
        #filter_query = "Date like '%{0}%'".format(TodaysDate)
        self.display_bookings = DisplayTable()
        self.display_bookings.show_results(bookingQuery)
        #self.display_bookings.model.setFilter(filter_query)
        
        #connections

        self.manage_bookings.clicked.connect(self.manage_booking_connect)


        #add widgets to booking layout
        self.todays_bookings_label = QLabel("Todays Bookings")
        self.todays_bookings_label.setFont(self.titleFont)
        self.todays_bookings_label.setFixedWidth(400)
        
        self.booking_layout.addWidget(self.todays_bookings_label)
        self.booking_layout.addWidget(self.display_bookings)
        self.booking_layout.addWidget(self.manage_bookings)
        
        

        #add layouts to main layout
        self.main_layout.addLayout(self.table_radio_layout)
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
        self.add_item_menu_bar.refresh

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
            self.delete_item_menu_bar = DisplayTable()
        self.delete_item_menu_bar.show_table("Items")
        self.delete_item_menu_bar.refresh
        self.delete_item_layout = QVBoxLayout()
        self.delete_item_layout.addWidget(self.delete_item_menu_bar )
        self.delete_item_layout.addWidget(self.delete_menu_item)
        self.delete_item_widget = QWidget()
        self.delete_item_widget.setLayout(self.delete_item_layout)
        self.stacked_layout.addWidget(self.delete_item_widget)
        self.delete_menu_item.itemDeleted.connect(self.delete_item_menu_bar.refresh) 
    

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

        self.view_dishes_tool = DisplayTable()
        self.view_dishes_tool.show_table("Items")
        self.view_dishes_tool.model.setFilter(filter_query)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.view_dishes_tool)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.stacked_layout.addWidget(self.main_widget) 
      

    def view_dishes_connect(self):
        self.stacked_layout.setCurrentIndex(9)

    def view_drinks_stack_layout(self):
        filter_query = "ItemTypeID like '%2%'"

        self.view_drinks_tool = DisplayTable()
        self.view_drinks_tool.show_table("Items")
        self.view_drinks_tool.model.setFilter(filter_query)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.view_drinks_tool)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.stacked_layout.addWidget(self.main_widget) 
     

    def view_drinks_connect(self):
        self.stacked_layout.setCurrentIndex(10)


def main():
    restaurant_simulation = QApplication(sys.argv) # create new application
    restaurant_window = RestaurantWindow() #create new instance of main window
    restaurant_window.show() #make instance visible
    restaurant_window.raise_() #raise instance to top of window stack
    restaurant_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()
