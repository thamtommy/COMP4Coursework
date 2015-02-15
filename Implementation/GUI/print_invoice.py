from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class PrintInvoice(QDialog):
    """This class provides a dialog box for getting email information"""
    def __init__(self):
        super().__init__()

        self.print_preview()

    def create_html(self):
        quantity = [1,2,3,4,5]
        items = ["Milk","Beef","Rice","Egg rice","Poo"]
        html = ""
        html += """<html>
<head>
<style>
	table, th, td
		{
			border: 1px solid black;
			border-collapse: collapse;
			width: 100%;
		}
	th, td
		{
			padding: 15px;
			text-align: center;
		}
</style>
</head>
<body>"""

        html += """<h1>Linhs Retaurant</h1>"""

        html += """<h2>Test</h2>
  <p></p>
   <table>
   <tr>
    <th>Quantity</th>
    <th>Item</th>
    <th>Price (£)</th>
   </tr>"""
   
        for each in quantity:   
            html += """<tr>
                       <td>{0}</td>
                       </tr>""".format(each)

        html += """<tr><td>Smith</td>
    <td>£30</td>
    </tr>
   <tr>
    <td>Edwin</td>
    <td>Jacobs</td>
    <td>£22</td>
   </tr>
   </table>
</body>
</html>"""
        return html
    
    def print_preview(self):
        html = self.create_html()
        document = QTextDocument()
        document.setHtml(html)
        print(html)
        self.printer = QPrinter()
        PrintPreview = QPrintPreviewDialog(self.printer, self)
        PrintPreview.paintRequested.connect(document.print_)
        PrintPreview.resize(1600,1000)
        PrintPreview.exec()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = PrintInvoice()
    window.show()
    window.raise_()
    application.exec()
