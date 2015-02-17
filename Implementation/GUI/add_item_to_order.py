import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from table_display import *

class AddItemToMenu(QDialog):
    itemAdded = pyqtSignal()
    """this class creates a window to add bookings"""

    def __init__(self,bookingDetails):
        super().__init__()
        #self.setWindowTitle("Add Item To Menu")
        self.bookingDetails = bookingDetails
        print("Here are the booking details {0}".format(bookingDetails))
        #create layouts
        self.main_layout = QVBoxLayout()
        self.add_item_layout = QGridLayout()
        self.add_complete_layout = QHBoxLayout()
        
        
        #create buttons
        self.add_complete = QPushButton("Add Item")

       
        #labels
        self.itemID_label = QLabel("Item ID : ")
        self.itemQuantity_label = QLabel("Item Quantity : ")

        #line edit

        regexp = QRegExp("^\\d\\d?$")
        validator = QRegExpValidator(regexp)
        self.input_itemID = QLineEdit()
        self.input_itemID.setValidator(validator)
        self.input_itemID.setMaximumSize(300,30)
        self.input_itemQuantity = QLineEdit()

        #table
        self.item_table = DisplayTable()
        self.item_table.show_table("Items")
        

        #add labels to layout
        self.add_item_layout.addWidget(self.itemID_label,0,0)
        self.add_item_layout.addWidget(self.itemQuantity_label,1,0)
        #add line edit to layout
        self.add_item_layout.addWidget(self.input_itemID,0,1)
        self.add_item_layout.addWidget(self.input_itemQuantity,1,1)
        #add button to layout
        self.add_complete_layout.addWidget(self.add_complete)
        #add layouts to main layout
        self.main_layout.addWidget(self.item_table)
        self.main_layout.addLayout(self.add_item_layout)
        self.main_layout.addLayout(self.add_complete_layout)


        #create a widget to display main layout
        self.setLayout(self.main_layout)

        #connections
        self.add_complete.clicked.connect(self.add_item_to_menu)

    def add_item_to_menu(self,bookingDetails):
        bookingID = self.bookingDetails[0]
        print("i am adding an item to {0}".format(bookingID))
        self.ItemID = self.input_itemID.text()
        Quantity = self.input_itemQuantity.text()

        MenuItem = (bookingID,self.ItemID,Quantity)

        addedAlready = self.checkExistingItem

        if addedAlready == True:
            with sqlite3.connect("restaurant.db") as db:
                cursor = db.cursor()
                cursor.execute("select Quantity from Booking_Items where ItemID=? and BookingID = ?",(self.ItemID,bookingID))
                dbquantity = cursor.fetchone()
                
            
            newQuantity = dbquantity + Quantity
            updateOrder = (newQuantity,self.ItemID)
            with sqlite3.connect("restaurant.db") as db:
                cursor = db.cursor()
                sql = "update Booking_Items set Quantity=? where ItemID=?"
                cursor.execute(sql,updateOrder)
                db.commit()

        elif addedAlready == False:

            with sqlite3.connect("restaurant.db") as db:
                cursor = db.cursor()
                sql = "insert into Booking_Items(BookingID,ItemID,Quantity) values (?,?,?)"
                cursor.execute(sql,MenuItem)
                db.commit()

            self.itemAdded.emit()

    def checkExistingItem(self):
        addedAlready = False
        itemsOrdered = []
        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("""SELECT
                            Items.ItemName
                            FROM Items
                            INNER JOIN Booking_Items
                            ON Booking_Items.ItemID = Items.ItemID
                            WHERE Booking_Items.BookingID = ? """,(self.bookingDetails[0],))
            items = cursor.fetchall()
            for each in items:
                itemsOrdered.append(each[0])

        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("""SELECT
                            Items.ItemName
                            FROM Items
                            INNER JOIN Booking_Items
                            ON Booking_Items.ItemID = Items.ItemID
                            WHERE Booking_Items.BookingID = ?
                            AND Items.ItemID = ?""",(self.bookingDetails[0],self.ItemID))
            item = cursor.fetchone()

        if len(item) > 0 :
            if item in itemsOrdered:
                addedAlready = True

        return addedAlready
        
            
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = AddItemToMenu(bookingDetails)
    window.show()
    window.raise_()
    application.exec()
                             

