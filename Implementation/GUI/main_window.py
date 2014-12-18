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
        self.initialUI()

    def initialUI(self):
        self.hello_radio_button = RadioButtonWidget("Hello","Moo", ("Drink","Dish"))
        self.instantiate_button = QPushButton("Blob")
        
        self.initial_layout = QGridLayout()
        self.initial_layout.addWidget(self.hello_radio_button)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_widget = QWidget()
        self.select_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.select_widget)

def main():
    restaurant_simulation = QApplication(sys.argv) # create new application
    restaurant_window = RestaurantWindow() #create new instance of main window
    restaurant_window.show() #make instance visible
    restaurant_window.raise_() #raise instance to top of window stack
    restaurant_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()
