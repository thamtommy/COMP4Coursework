import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from table_display import *
from cascade_style_sheet import *

class AddItemToOrder(QDialog):
    orderitemAdded = pyqtSignal()
    """this class creates a widget to add an item to order"""

    def __init__(self,bookingDetails):
        super().__init__()
        self.setWindowTitle("Add Item To Order")
        self.setMinimumSize(600,600)
        self.bookingDetails = bookingDetails
        self.setStyleSheet(css)
   
        self.main_layout = QVBoxLayout()
        self.add_item_layout = QGridLayout()
        self.add_complete_layout = QHBoxLayout()
        
        self.add_complete = QPushButton("Add Item")
        self.itemID_label = QLabel("Item ID : ")
        self.itemQuantity_label = QLabel("Item Quantity : ")

        #line edit
        regexp = QRegExp("^\\d\\d\\d?$")
        validator = QRegExpValidator(regexp)
        self.input_itemID = QLineEdit()
        self.input_itemID.setValidator(validator)
        self.input_itemID.setMaximumSize(133,30)
        self.input_itemID.setAlignment(Qt.AlignLeft)
        self.input_itemQuantity = QLineEdit()
        self.input_itemQuantity.setValidator(validator)
        self.input_itemQuantity.setMaximumSize(133,30)

        self.item_table = DisplayTable()
        self.item_table.show_table("Items")
        

        self.add_item_layout.addWidget(self.itemID_label,0,0)
        self.add_item_layout.addWidget(self.itemQuantity_label,1,0)
        self.add_item_layout.addWidget(self.input_itemID,0,1)
        self.add_item_layout.addWidget(self.input_itemQuantity,1,1)
        self.add_complete_layout.addWidget(self.add_complete)
    
        self.main_layout.addWidget(self.item_table)
        self.main_layout.addLayout(self.add_item_layout)
        self.main_layout.addLayout(self.add_complete_layout)

        self.setLayout(self.main_layout)

        self.add_complete.clicked.connect(self.add_item_to_order)

    def add_item_to_order(self,bookingDetails):
        bookingID = self.bookingDetails[0]
        self.ItemID = self.input_itemID.text()
        Quantity = self.input_itemQuantity.text()
        MenuItem = (bookingID,self.ItemID,Quantity)
        addedAlready = self.checkExistingItem()
        print(addedAlready)

        try:

            if addedAlready == True:
                with sqlite3.connect("restaurant.db") as db:
                    cursor = db.cursor()
                    cursor.execute("select Quantity from Booking_Items where ItemID=? and BookingID = ?",(self.ItemID, bookingID))
                    dbquantity = cursor.fetchone()[0]
                    
                newQuantity = dbquantity + int(Quantity)
                updateOrder = (newQuantity,self.ItemID)
                with sqlite3.connect("restaurant.db") as db:
                    cursor = db.cursor()
                    sql = "update Booking_Items set Quantity=? where ItemID=?"
                    cursor.execute("PRAGMA foreign_keys = ON")
                    cursor.execute(sql,updateOrder)
                    db.commit()
                    
                self.orderitemAdded.emit()

            elif addedAlready == False:

                with sqlite3.connect("restaurant.db") as db:
                    cursor = db.cursor()
                    sql = "insert into Booking_Items(BookingID,ItemID,Quantity) values (?,?,?)"
                    cursor.execute("PRAGMA foreign_keys = ON")
                    cursor.execute(sql,MenuItem)
                    db.commit()

                self.orderitemAdded.emit()
        except sqlite3.IntegrityError:
             QMessageBox.about(self, "Error", "Please make sure the item exists")

    def checkExistingItem(self):
        addedAlready = False
        itemsOrdered = []
        item = ""
        
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("""SELECT
                            Items.ItemName
                            FROM Items
                            INNER JOIN Booking_Items
                            ON Booking_Items.ItemID = Items.ItemID
                            WHERE Booking_Items.BookingID = ? """, (self.bookingDetails[0],))
            items = cursor.fetchall()
            for each in items:
                itemsOrdered.append(each[0])

        try:
            with sqlite3.connect("restaurant.db") as db:
                cursor = db.cursor()
                cursor.execute("""SELECT
                                Items.ItemName
                                FROM Items
                                INNER JOIN Booking_Items
                                ON Booking_Items.ItemID = Items.ItemID
                                WHERE Booking_Items.BookingID = ?
                                AND Items.ItemID = ?""", (self.bookingDetails[0], self.ItemID))
                item = cursor.fetchone()[0]
        except TypeError:
            pass
  
        if item in itemsOrdered:
            addedAlready = True

        return addedAlready

        
                             

