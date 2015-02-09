import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AddItemToMenu(QWidget):
    itemAdded = pyqtSignal()
    """this class creates a window to add bookings"""

    def __init__(self):
        super().__init__()
        #self.setWindowTitle("Add Item To Menu")

        #create layouts
        self.main_layout = QVBoxLayout()
        self.add_item_layout = QGridLayout()
        self.add_complete_layout = QHBoxLayout()
        
        
        #create buttons
        self.add_complete = QPushButton("Add Item")

        #create combobox for item type
        self.select_item_type = QComboBox(self)
        self.select_item_type.addItem("Dish")
        self.select_item_type.addItem("Drink")
         
        
        #labels
        self.item_name_label = QLabel("Item Name : ")
        self.item_price_label = QLabel("Item Price : ")
        self.item_type_label = QLabel("Item Type : ")

        #line edit
        self.input_item_name = QLineEdit()
        self.input_item_name.setMaximumSize(300,30)

        regexp = QRegExp("^\\d\\d?$")
        validator = QRegExpValidator(regexp)
        self.input_item_price = QLineEdit()
        self.input_item_price.setValidator(validator)
        self.input_item_price.setMaximumSize(300,30)

        #add labels to layout
        self.add_item_layout.addWidget(self.item_name_label,0,0)
        self.add_item_layout.addWidget(self.item_price_label,1,0)
        self.add_item_layout.addWidget(self.item_type_label,2,0)

        #add line edit to layout
        self.add_item_layout.addWidget(self.input_item_name,0,1)
        self.add_item_layout.addWidget(self.input_item_price,1,1)
        self.add_item_layout.addWidget(self.select_item_type,2,1)

        #add button to layout
        self.add_complete_layout.addWidget(self.add_complete)
        
        #add layouts to main layout
        self.main_layout.addLayout(self.add_item_layout)
        self.main_layout.addLayout(self.add_complete_layout)


        #create a widget to display main layout
        self.setLayout(self.main_layout)

        #connections
        self.add_complete.clicked.connect(self.add_item_to_menu)

    def add_item_to_menu(self):
        ItemName = self.input_item_name.text()
        ItemPrice = self.input_item_price.text()
        ItemType = self.select_item_type.currentIndex()
        if ItemType == 0:
            ItemType = 1
        else:
            ItemType = 2
        MenuItem = (ItemName,ItemPrice,ItemType)
        print(MenuItem)
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            sql = "insert into Items(ItemName,ItemPrice,ItemTypeID) values (?,?,?)"
            cursor.execute(sql,MenuItem)
            db.commit()

        self.itemAdded.emit()
            
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = AddItemToMenu()
    window.show()
    window.raise_()
    application.exec()
                             

