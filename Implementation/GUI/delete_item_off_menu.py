import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from table_display import *

class DeleteItemOffMenu(QWidget):
    """this class creates a widget to delete items off the menu"""

    def __init__(self):
        super().__init__()
        self.display_table = DisplayTable()
        self.display_table.show_table("Items")

        #create layouts
        self.main_layout = QVBoxLayout()
        self.delete_item_name_layout = QHBoxLayout()
        self.delete_itemID_layout = QHBoxLayout()
        
        
        #create buttons
        self.delete_item_name = QPushButton("Delete Item")
        self.delete_itemID = QPushButton("Delete Item")
       
        
        #labels
        self.item_name_label = QLabel("Item Name : ")
        self.itemID_label = QLabel("Item ID : ")


        #line edit
        self.input_item_name = QLineEdit()
        self.input_item_name.setMaximumSize(300,30)

        regexp = QRegExp("^\\d\\d\\d?$")
        validator = QRegExpValidator(regexp)
        self.input_itemID = QLineEdit()
        self.input_itemID.setValidator(validator)
        self.input_itemID.setMaximumSize(300,30)

        #add widgets to delete item name layout
        self.delete_item_name_layout.addWidget(self.item_name_label)
        self.delete_item_name_layout.addWidget(self.input_item_name)
        self.delete_item_name_layout.addWidget(self.delete_item_name)

        #add widgets to delete itemID layout
        self.delete_itemID_layout.addWidget(self.itemID_label)
        self.delete_itemID_layout.addWidget(self.input_itemID)
        self.delete_itemID_layout.addWidget(self.delete_itemID)
        
        #add layouts to main layout
        self.main_layout.addWidget(self.display_table)
        self.main_layout.addLayout(self.delete_item_name_layout)
        self.main_layout.addLayout(self.delete_itemID_layout)


        #set layout
        self.setLayout(self.main_layout)

        #connections
        self.delete_item_name.clicked.connect(self.delete_item_off_menu)
        self.delete_itemID.clicked.connect(self.delete_itemID_off_menu)

    def delete_item_off_menu(self):
        item_name = self.input_item_name.text()
        print(item_name)
        if len(item_name)>1:
            item_name = (item_name,)
            with sqlite3.connect("restaurant.db") as db:
                cursor = db.cursor()
                sql = "delete from Items where ItemName = ?"
                cursor.execute(sql,item_name)
                db.commit()

            self.display_table.refresh()
        else:
            QMessageBox.about(self,"Error","Please make sure you have filled in the required field ")

    def delete_itemID_off_menu(self):
        itemID = self.input_itemID.text()
        print(itemID)
        try:
            
            with sqlite3.connect("restaurant.db") as db:
                cursor = db.cursor()
                sql = ("delete from Items where ItemID = {0}".format(itemID))
                cursor.execute(sql)
                db.commit()

            self.display_table.refresh()

        except (sqlite3.OperationalError) or AttributeError:
            QMessageBox.about(self,"Error","Please make sure you have filled in the required field correctly")
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = DeleteItemOffMenu()
    window.show()
    window.raise_()
    application.exec()
                             

