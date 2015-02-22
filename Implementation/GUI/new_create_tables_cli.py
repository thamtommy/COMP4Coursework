import sqlite3


def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it (y/n): ".format(table_name))
            if response == 'y':
                keep_table = False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table = False
        if not keep_table:  
            cursor.execute(sql)
            db.commit()

def Type():
    sql = """create table ItemType
             (ItemTypeID integer,
             Type text,
             primary key(ItemTypeID))"""            
    create_table(db_name,"ItemType",sql)

def Items():
    sql = """create table Items
             (ItemID integer,
             ItemName text,
             ItemPrice real,
             ItemTypeID integer,
             primary key(ItemID),
             foreign key(ItemTypeID) references ItemType(ItemTypeID))"""  
    create_table(db_name,"Items",sql)

def BookingItem():
    sql = """create table Booking_Items
             (BookingItemID integer,
             BookingID integer,
             ItemID integer,
             Quantity integer,
             primary key(BookingItemID),
             foreign key(BookingID) references Booking(BookingID),
             foreign key(ItemID) references Items(ItemID))"""
    create_table(db_name,"Booking_Items",sql)
             

def Booking():
    sql = """create table Bookings
             (BookingID integer,
             CustomerID integer,
             TableNumber integer,
             NumberOfPeople integer,
             Date text,
             Time text,
             primary key(BookingID),
             foreign key(CustomerID) references Customers(CustomerID),
             foreign key(TableNumber) references Table_Numbers(TableNumber))"""
    create_table(db_name,"Bookings",sql)

def Table():
    sql = """create table Table_Numbers
          (TableNumber integer,
          MaxNumberOfPeople integer,
          primary key(TableNumber))"""
    create_table(db_name,"Table_Numbers",sql)

#create a customer id for a walk in
def Customer():
    sql = """create table Customers
             (CustomerID integer,
             FirstName text,
             LastName text,
             TelephoneNo integer,
             primary key(CustomerID))"""
    create_table(db_name,"Customers",sql)         

    
if __name__ == "__main__":
    db_name = "restaurant.db"
    Type()
    Items()
    BookingItem()
    Booking()
    Table()
    Customer()
    data = ("Street","Customer","None")
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        sql = "insert into Customers (FirstName,LastName,TelephoneNo) values (?,?,?)"
        cursor.execute(sql,data)
        db.commit()

    
        
