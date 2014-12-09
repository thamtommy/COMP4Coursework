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
             primary key(ItemTypeID))"""
    create_table(db_name,"ItemType",sql)

def Reservation():
    sql = """create table Reservation
             (ReservationID integer,
             FirstName text,
             LastName text,
             TelephoneNo text,
             primary key(ReservationID))"""
    create_table(db_name,"Reservation",sql)

def OrderID():
    sql = """create table Orders
             (OrderID integer,
             TotalDrinkPrice real,
             TotalDishPrice real,
             TotalPrice real,
             primary key(OrderID))"""
    create_table(db_name,"Orders",sql)
    
def MenuID():
    sql = """create table Menu
             (MenuID integer,
             MenuItem text,
             ItemPrice real,
             ItemType text,
             primary key(MenuID)
             foreign key(ItemType) references ItemType(ItemType)
             on update cascade on delete cascade)"""
    
    create_table(db_name,"Menu",sql)             

def OrderItemID():
    sql = """create table Ordered_Items
             (OrderItemID integer,
             OrderID integer,
             MenuID integer,
             Quantity integer,
             primary key(OrderItemID),
             foreign key(OrderID) references Orders(OrderID),
             foreign key(MenuID) references Menu(MenuID))"""
    create_table(db_name,"Ordered_Items",sql)

def CustomerID():
    sql = """create table Customer
             (CustomerID integer,
             ReservationID integer,
             OrderID integer,
             NumberOfPeople integer,
             Date text,
             Time text,
             TableNumber integer,
             primary key(CustomerID),
             foreign key(ReservationID) references Reservation(ReservationID),
             foreign key(OrderID) references Orders(OrderID))"""
    create_table(db_name,"Customer",sql)
             
    
if __name__ == "__main__":
    db_name = "restaurant.db"
    Type()
    Reservation()
    OrderID()
    MenuID()
    OrderItemID()
    CustomerID()
    
        
    
