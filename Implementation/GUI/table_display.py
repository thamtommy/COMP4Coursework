import sys
import sqlite3

from PyQt4.QtSql import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DisplayTable(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.db = None
        self.model = None
        self.open_database()


    def display_results_layout(self):
        self.results_table = QTableView()
        self.results_layout = QVBoxLayout()
        self.results_layout.addWidget(self.results_table)
        self.results_widget = QWidget()
        self.results_widget.setLayout(self.results_layout)
        self.stacked_layout.addWidget(self.results_widget)

    def open_database(self):
        if self.db:
            self.close_database()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("restaurant.db")
        opened_ok = self.db.open()
        return opened_ok

    def show_results(self,query):
        self.display_results_layout()
        if not self.model or not isinstance(self.model,QSqlQueryModel):
            self.model = QSqlQueryModel()
        self.model.setQuery(query)
        self.results_table.setModel(self.model)
        self.results_table.show()

    def show_table(self,tableName):
        self.display_results_layout()
        if not self.model or not isinstance(self.model,QSqlTableModel):
            self.model = QSqlTableModel()
        self.model.setTable(tableName)
        self.model.select()
        self.results_table.setModel(self.model)
        self.results_table.show()

    def refresh(self):
        
        print("here")
        self.results_table.setModel(self.model)
        self.results_table.show()
        #print(self.model.lastError().text())
        self.model.select()
        #self.model.emit()
        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = DisplayTable()
    window.show()
    window.raise_()
    application.exec()
