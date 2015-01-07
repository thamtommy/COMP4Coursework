import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button_widget_class import *

class OrderWindow(QMainWindow):
    """this class creates a main window to observe the restaurant"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage Order")
        self.create_manage_order_layout()
        
    def create_manage_order_layout(self):
        #create buttons
        self.back_button = QPushButton("Back") # Will be an arrow
        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete")
        self.finish_button = QPushButton("Finish")

        #connections
        self.add_button.clicked.connect(self.DrinkorDish)

        #create labels
        self.drinks_label = QLabel("Drinks")
        self.dishes_label = QLabel("Dishes")
        self.table_number_label = QLabel("Table : ")
        self.date_label = QLabel("Date : ")
        self.time_label = QLabel("Time : ")
        self.number_people_label = QLabel("Number of people : ")
        
        
        

        #create layouts
        self.order_layout = QVBoxLayout()
        self.order_information = QGridLayout()
        self.items_ordered = QGridLayout()
        self.manage_order = QHBoxLayout()

        #add buttons to layouts
        self.manage_order.addWidget(self.add_button)
        
        self.manage_order.addWidget(self.delete_button)
        self.manage_order.addWidget(self.finish_button)

        #labels to item ordered layout
        self.items_ordered.addWidget(self.dishes_label,0,0)
        self.items_ordered.addWidget(self.drinks_label,0,1)

            #labels to order information
        self.order_information.addWidget(self.table_number_label,0,1)
        self.order_information.addWidget(self.date_label,2,0)
        self.order_information.addWidget(self.time_label,2,1)
        self.order_information.addWidget(self.number_people_label,2,2)

        #add layouts to main order layout
        self.order_layout.addLayout(self.order_information)
        self.order_layout.addLayout(self.items_ordered)
        self.order_layout.addLayout(self.manage_order)

        #create widget to display main order layout
        self.view_order_widget = QWidget()
        self.view_order_widget.setLayout(self.order_layout)
        self.setCentralWidget(self.view_order_widget)

    def DrinkorDish(self): 
        self.hello_radio_button = RadioButtonWidget("Item type","Please select an item type",("Drink","Dish"))
        self.instantiate_button = QPushButton("Add")
        
        self.initial_layout = QGridLayout()
        self.initial_layout.addWidget(self.hello_radio_button)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_widget = QWidget()
        self.select_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.select_widget)
        

def main():
    order_manage = QApplication(sys.argv) # create new application
    order_window = OrderWindow() #create new instance of main window
    order_window.show() #make instance visible
    order_window.raise_() #raise instance to top of window stack
    order_manage.exec_() #monitor application for events

if __name__ == "__main__":
    main()

