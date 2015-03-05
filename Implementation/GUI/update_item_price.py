import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from table_display import *

class UpdateItemPrice(QDialog):
    """this class creates a widget to update prices of items on the menu"""

    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.update_item_layout = QGridLayout()
        self.update_complete_layout = QHBoxLayout()
        
        self.display_table = DisplayTable()
        self.display_table.show_table("Items")
        
        self.update_complete = QPushButton("Update Item")
    
        self.itemID_label = QLabel("Item ID : ")
        self.item_price_label = QLabel("New Item Price : ")


        regexp = QRegExp("^\\d\\d\\d?$")
        validator = QRegExpValidator(regexp)
        self.input_itemID = QLineEdit()
        self.input_itemID.setValidator(validator)
        self.input_itemID.setMaximumSize(300,30)

        regexp2 = QRegExp("(^\d|\d\d)(\.\d\d)?$")
        validator2 = QRegExpValidator(regexp2)
        self.input_item_price = QLineEdit()
        self.input_item_price.setValidator(validator2)
        self.input_item_price.setMaximumSize(300,30)


        self.update_item_layout.addWidget(self.itemID_label,0,0)
        self.update_item_layout.addWidget(self.item_price_label,1,0)
        self.update_item_layout.addWidget(self.input_itemID,0,1)
        self.update_item_layout.addWidget(self.input_item_price,1,1)
        self.update_complete_layout.addWidget(self.update_complete)
        
        self.main_layout.addWidget(self.display_table)
        self.main_layout.addLayout(self.update_item_layout)
        self.main_layout.addLayout(self.update_complete_layout)

        self.setLayout(self.main_layout)

        #connection
        self.update_complete.clicked.connect(self.update_item)

    def update_item(self):
        ItemID = self.input_itemID.text()
        ItemPrice = self.input_item_price.text()
        UpdateItem = (ItemPrice,ItemID)
        print(UpdateItem)
        if len(ItemID)>0 and (len(ItemPrice)>0):
            
            with sqlite3.connect("restaurant.db") as db:
                cursor = db.cursor()
                sql = "update Items set ItemPrice=? where ItemID=?"
                cursor.execute("PRAGMA foreign_keys = ON")
                cursor.execute(sql,UpdateItem)
                db.commit()

            self.display_table.refresh()
        else:
            QMessageBox.about(self,"Error","Please fill in the required fields")
        
     
            
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = UpdateItemPrice()
    window.show()
    window.raise_()
    application.exec()
                             

