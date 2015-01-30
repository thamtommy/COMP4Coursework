import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class UpdateItemPrice(QDialog):
    """this class creates a window to add bookings"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Item Price")

        #create layouts
        self.main_layout = QVBoxLayout()
        self.update_item_layout = QGridLayout()
        self.update_complete_layout = QHBoxLayout()
        
        
        #create buttons
        self.update_complete = QPushButton("Update Item")


    
        #labels
        self.itemID_label = QLabel("Item ID : ")
        self.item_price_label = QLabel("New Item Price : ")


        #line edit
        self.input_itemID = QLineEdit()
        self.input_itemID.setMaximumSize(300,30)

        self.input_item_price = QLineEdit()
        self.input_item_price.setMaximumSize(300,30)

        #add labels to layout
        self.update_item_layout.addWidget(self.itemID_label,0,0)
        self.update_item_layout.addWidget(self.item_price_label,1,0)


        #add line edit to layout
        self.update_item_layout.addWidget(self.input_itemID,0,1)
        self.update_item_layout.addWidget(self.input_item_price,1,1)


        #add button to layout
        self.update_complete_layout.addWidget(self.update_complete)
        
        #add layouts to main layout
        self.main_layout.addLayout(self.update_item_layout)
        self.main_layout.addLayout(self.update_complete_layout)


        #create a widget to display main layout
        self.setLayout(self.main_layout)

        #connections
        self.update_complete.clicked.connect(self.update_item)

    def update_item(self):
        ItemID = self.input_itemID.text()
        ItemPrice = self.input_item_price.text()
        UpdateItem = (ItemPrice,ItemID)
        print(UpdateItem)
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            sql = "update Items set ItemPrice=? where ItemID=?"
            cursor.execute(sql,UpdateItem)
            db.commit()
            
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = UpdateItemPrice()
    window.show()
    window.raise_()
    application.exec()
                             

