import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class CustomerInvoice(QDialog):
    """This class provides a dialog box for getting email information"""
    def __init__(self,bookingDetails):
        super().__init__()
        self.bookingDetails = bookingDetails
        self.bookingNo = self.bookingDetails[0] #bookingID
        print(self.bookingNo)
        self.TableNo = self.bookingDetails[2]
        self.Date = self.bookingDetails[4]
        self.Time = self.bookingDetails[5]

        self.items = []
        self.price = []
        self.quantity = []


        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("""SELECT
                            Items.ItemName
                            FROM Items
                            INNER JOIN Booking_Items
                            ON Booking_Items.ItemID = Items.ItemID
                            WHERE Booking_Items.BookingID = ? """,(self.bookingNo,))
            items = cursor.fetchall()
            for each in items:
                self.items.append(each[0])

        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("""SELECT
                            Items.ItemPrice
                            FROM Items
                            INNER JOIN Booking_Items
                            ON Booking_Items.ItemID = Items.ItemID
                            WHERE Booking_Items.BookingID = ? """,(self.bookingNo,))
            price = cursor.fetchall()
            for each in price:
                self.price.append(each[0])

        with sqlite3.connect("restaurant.db") as db:
            cursor = db.cursor()
            cursor.execute("""SELECT
                            Booking_Items.Quantity
                            FROM Items
                            INNER JOIN Booking_Items
                            ON Booking_Items.ItemID = Items.ItemID
                            WHERE Booking_Items.BookingID = ? """,(self.bookingNo,))
            quantity = cursor.fetchall()
            for each in quantity:
                self.quantity.append(each[0])


        for each in range (len(self.price)):
            print(each)
            self.price[each] = self.price[each]*self.quantity[each]

        

    def create_html(self):
        TotalPrice = 0
        for each in self.price:
            TotalPrice += each
        html = ""
        html += """
<html>
<head>
<style>
table, th, td {
		
    border: 3px solid black;
    border-collapse: collapse;
    width: 100%;
}
	th, td
		{
			padding: 10px;
			text-align: center;
		}


</style>
</head>
<body>"""

        html += """<center> <h1>Linhs Chinese Retaurant</h1> </center>"""
        html += """ <p align = "right">
                <br> 48A CARTER STREET <br>
                FORDHAM - ELY <br>
                CAMBRIDGESHIRE <br>
                TEL: (01638) 721117 <br>
                </p>
                """

        html += """<p>
                <b>Date</b> &nbsp;{0} <br>
                <b>Time</b> &nbsp; {1} <br> <br>
                <b>Table Number</b> &nbsp; {2} <br>
                <b>Booking No.</b> &nbsp; {3}
                  <p></p>
                   <table style = "width:100%", align="center">
                   <tr>
                    <th>Quantity</th>
                    <th>Item</th>
                    <th>Price (£)</th>
                   </tr>""".format(self.Date,self.Time,self.TableNo,self.bookingNo)
        
        for count in range (len(self.items)):
            html += """<tr>
                       <td>{0}</td>
                       <td>{1}</td>
                       <td>{2}</td>
                       </tr>
                       """.format(self.quantity[count],self.items[count],self.price[count])

        html+="""

   </table>
   
   <br>
   <br> """
        html +=""" <center><b>   Total Price</b> : £ {0}</center> 
   <br>
   <br>
   <em>All meal rates are invlusive of VAT <br>
   There is no Service Charge</em>
</body>
</html>""".format(TotalPrice)
        return html
    
    def print_preview(self):
        html = self.create_html()
        document = QTextDocument()
        document.setHtml(html)
        self.printer = QPrinter()
        self.printer.setPaperSize(QSizeF(200, 220), QPrinter.Millimeter)
        invoicePreview = QPrintPreviewDialog(self.printer, self)
        invoicePreview.paintRequested.connect(document.print_)
        invoicePreview.resize(1280,900)
        invoicePreview.exec()


    def print_invoice(self):
        html = self.create_html()
        self.printer = QPrinter()
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            document = QTextDocument()
            document.setHtml(html)
            document.print_(self.printer)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = CustomerInvoice()
    window.show()
    window.raise_()
    application.exec()
