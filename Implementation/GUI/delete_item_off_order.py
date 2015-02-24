import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from table_display import *

class DeleteItemOffOrder(QDialog):
    orderitemDeleted = pyqtSignal()
    """this class creates a window to add an item to order"""

    def __init__(self,bookingDetails):
        super().__init__()
        self.setWindowTitle("Delete Item Off Order")
        self.bookingDetails = bookingDetails
        self.setMinimumSize(600,600)
        #create layouts
        self.main_layout = QVBoxLayout()
        self.delete_item_layout = QGridLayout()
        self.delete_complete_layout = QHBoxLayout()
        
        
        #create buttons
        self.delete_complete = QPushButton("Delete Item")

       
        #labels
        self.itemID_label = QLabel("Item ID : ")
        self.itemQuantity_label = QLabel("Item Quantity : ")

        #line edit

        regexp = QRegExp("^\\d\\d\\d?$")
        validator = QRegExpValidator(regexp)
        self.input_itemID = QLineEdit()
        self.input_itemID.setValidator(validator)
        self.input_itemID.setMaximumSize(300,30)
        self.input_itemQuantity = QLineEdit()
        self.input_itemQuantity.setValidator(validator)
        self.input_itemQuantity.setMaximumSize(300,30)

        #table
        self.item_table = DisplayTable()
        query = """SELECT
                        Booking_Items.Quantity,
                        Items.ItemID,
                        Items.ItemName,
                        Items.ItemPrice
                        FROM Items
                        INNER JOIN Booking_Items
                        ON Booking_Items.ItemID = Items.ItemID
                        WHERE Booking_Items.BookingID = {0}
                        """.format(self.bookingDetails[0]) 
        self.item_table.show_results(query)
        

        #add labels to layout
        self.delete_item_layout.addWidget(self.itemID_label,0,0)
        self.delete_item_layout.addWidget(self.itemQuantity_label,1,0)
        #add line edit to layout
        self.delete_item_layout.addWidget(self.input_itemID,0,1)
        self.delete_item_layout.addWidget(self.input_itemQuantity,1,1)
        #add button to layout
        self.delete_complete_layout.addWidget(self.delete_complete)
        #add layouts to main layout
        self.main_layout.addWidget(self.item_table)
        self.main_layout.addLayout(self.delete_item_layout)
        self.main_layout.addLayout(self.delete_complete_layout)


        #create a widget to display main layout
        self.setLayout(self.main_layout)

        #connections
        self.delete_complete.clicked.connect(self.delete_item_off_order)

    def delete_item_off_order(self,bookingDetails):
        self.bookingID = self.bookingDetails[0]
        self.ItemID = self.input_itemID.text()
        Quantity = self.input_itemQuantity.text()

        MenuItem = (self.bookingID,self.ItemID)

        OneQuantity = self.checkQuantity()

        if OneQuantity == False:
            with sqlite3.connect("restaurant.db") as db:
                cursor = db.cursor()
                cursor.execute("select Quantity from Booking_Items where ItemID=? and BookingID = ?",(self.ItemID,self.bookingID))
                dbquantity = cursor.fetchone()[0]
                
            newQuantity = dbquantity - int(Quantity)
            
            if newQuantity <= 0:
                
                with sqlite3.connect("restaurant.db") as db:
                    cursor = db.cursor()
                    sql = "delete from Booking_Items where BookingID = ? and ItemID = ? "
                    cursor.execute("PRAGMA foreign_keys = ON")
                    cursor.execute(sql,MenuItem)
                    db.commit()
            else:
                
                updateOrder = (newQuantity,self.ItemID)
                with sqlite3.connect("restaurant.db") as db:
                    cursor = db.cursor()
                    sql = "update Booking_Items set Quantity=? where ItemID=?"
                    cursor.execute("PRAGMA foreign_keys = ON")
                    cursor.execute(sql,updateOrder)
                    db.commit()
                
            self.orderitemDeleted.emit()

        elif OneQuantity == True:

            with sqlite3.connect("restaurant.db") as db:
                cursor = db.cursor()
                sql = "delete from Booking_Items where BookingID = ? and ItemID = ? "
                cursor.execute("PRAGMA foreign_keys = ON")
                cursor.execute(sql,MenuItem)
                db.commit()

            self.orderitemDeleted.emit()

    def checkQuantity(self):
        OneQuantity = False
        try:
            with sqlite3.connect("restaurant.db") as db:
                cursor = db.cursor()
                cursor.execute("""SELECT
                                Quantity
                                FROM Booking_Items
                                WHERE BookingID = ?
                                AND ItemID = ?""",(self.bookingID,self.ItemID))
                itemQuantity = cursor.fetchone()[0]
                print(itemQuantity)

            if (int(itemQuantity)) == 1:
                OneQuantity = True
                
            return OneQuantity
        except TypeError:
            pass
        
                             

