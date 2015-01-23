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
             ItemDescription text,
             ItemPrice real,
             ItemTypeID integer,
             primary key(ItemID),
             foreign key(ItemTypeID) references ItemType(ItemTypeID)
             on update cascade on delete cascade)"""  
    create_table(db_name,"Items",sql)

def BookingItem():
    sql = """create table BookingItems
             (BookingItemID integer,
             BookingID integer
             ItemID integer,
             Quantity integer,
             primary key(BookingItemID),
             foreign key(BookingID) references Booking(BookingID),
             foreign key(MenuID) references Menu(MenuID))"""
    create_table(db_name,"Ordered_Items",sql)
             

def Booking():
    sql = """create table Bookings
             (BookingID integer,
             CustomerID integer,
             TableNumber integer,
             NumberOfPeople integer,
             Date text,
             Time text,
             primary key(BookingID),
             foreign key(CustomerID) references Customers(CustomerID)"""
    create_table(db_name,"Bookings",sql)

def Table():
    sql = """create Table Number,
          (TableNumber integer)
          primary key (TableNumber))"""
    create_table(db_name,"Table Number",sql)

#create a customer id for a walk in
def Customer():
    sql = """create table Customers
             (CustomerID integer,
             FirstName text,
             LastName text,
             TelephoneNo integer,
             primary key(CustomerID))"""
    create_table(db_name,"Customer",sql)         

    
if __name__ == "__main__":
    db_name = "restaurant.db"
    Type()
    Booking()
    Menu()
    BookingItem()
    Customer()
    Table()
    
        
