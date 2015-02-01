#http://pyqt.sourceforge.net/Docs/PyQt4/qdate.html#currentDate

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class OrderWindow(QWidget):
    """this class creates a main window to observe the restaurant"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage Order")
        
        #create buttons
        self.back_button = QPushButton("Back") # Will be an arrow
        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete")
        self.finish_button = QPushButton("Finish")

        #connections
        self.add_button.clicked.connect(self.DrinkorDish)

        #date widget
        self.current_date = QDate.currentDate()

        #create labels
        self.drinks_label = QLabel("Drinks")
        self.dishes_label = QLabel("Dishes")
        self.table_number_label = QLabel("Table : ")
        self.date_label = QLabel("Date : {0} ".format(self.current_date))
        self.time_label = QLabel("Time : ")
        self.number_people_label = QLabel("Number of people : ")
        
        
        

        #create layouts
        self.order_layout = QVBoxLayout()
        self.order_information = QHBoxLayout()
        self.items_ordered = QGridLayout()
        self.dishes_ordered = QVBoxLayout()
        self.drinks_ordered = QVBoxLayout()
        self.manage_order = QHBoxLayout()

        #add buttons to layouts
        self.manage_order.addWidget(self.add_button)
        
        self.manage_order.addWidget(self.delete_button)
        self.manage_order.addWidget(self.finish_button)

        #labels
        ##labels to drink/dish
        self.dishes_ordered.addWidget(self.dishes_label)
        self.drinks_ordered.addWidget(self.drinks_label)
        ##labels to order information
        self.order_information.addWidget(self.table_number_label)
        self.order_information.addWidget(self.date_label)
        self.order_information.addWidget(self.time_label)
        self.order_information.addWidget(self.number_people_label)

        #layouts
        ##add layouts to items ordered layout
        self.items_ordered.addLayout(self.dishes_ordered,0,0)
        self.items_ordered.addLayout(self.drinks_ordered,0,1)
        ##add layouts to main order layout
        self.order_layout.addLayout(self.order_information)
        self.order_layout.addLayout(self.items_ordered)
        self.order_layout.addLayout(self.manage_order)

        #create widget to display main order layout

        self.setLayout(self.order_layout)

    def DrinkorDish(self): 
        self.hello_radio_button = RadioButtonWidget("Item type","Please select an item type",("Drink","Dish"))
        self.instantiate_button = QPushButton("Add")
        
        self.initial_layout = QGridLayout()
        self.initial_layout.addWidget(self.hello_radio_button)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_widget = QWidget()
        self.select_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.select_widget)
        

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = OrderWindow()
    window.show()
    window.raise_()
    application.exec()


