import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from table_display import *

class AddItemToMenu(QWidget):
    """this class creates a widget to add items to the menu"""

    def __init__(self):
        super().__init__()

        self.display_table = DisplayTable()
        self.display_table.show_table("Items")

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
        regexpp = QRegExp("[a-z | A-Z]{1,20}")
        validatorr = QRegExpValidator(regexpp)
        self.input_item_name = QLineEdit()
        self.input_item_name.setValidator(validatorr)
        self.input_item_name.setMaximumSize(300,30)

        regexp = QRegExp("(^\d|\d\d)(\.\d\d)?$")
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
        
        #add layouts/table to main layout
        self.main_layout.addWidget(self.display_table)
        self.main_layout.addLayout(self.add_item_layout)
        self.main_layout.addLayout(self.add_complete_layout)
        self.setLayout(self.main_layout)

        #connection
        self.add_complete.clicked.connect(self.add_item_to_menu)

        self.display_table.refresh()

    def add_item_to_menu(self):
        ItemName = self.input_item_name.text().capitalize()
        ItemPrice = self.input_item_price.text()
        ItemType = self.select_item_type.currentIndex()
        if ItemType == 0:
            ItemType = 1
        else:
            ItemType = 2
        MenuItem = (ItemName,ItemPrice,ItemType)
        print(MenuItem)
        if len(ItemName)>1 and (len(ItemPrice)>0):
            with sqlite3.connect("restaurant.db") as db:
                cursor = db.cursor()
                sql = "insert into Items(ItemName,ItemPrice,ItemTypeID) values (?,?,?)"
                cursor.execute("PRAGMA foreign_keys = ON")
                cursor.execute(sql,MenuItem)
                db.commit()

            self.display_table.refresh()
        else:
            QMessageBox.about(self, "Error","Please make sure you have filled in the required fields")



            
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = AddItemToMenu()
    window.show()
    window.raise_()
    application.exec()
                             

