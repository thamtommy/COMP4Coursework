from insert_product_data import *
from delete_exisiting_product import *
from select_existing_products import *
from update_product_data import *
from Database import * 

def display_menu():
    print("1. (Re)Create Product Table")
    print("2. Add new product")
    print("3. Edit existing product")
    print("4. Delete existing product")
    print("5. Search for products")
    print("0. Exit")
    print()

def select_option():
    choiceValid = False
    while not choiceValid:
        choice = int(input("Please select an option: "))
        if choice >= 0 and choice < 6:
            choiceValid = True
        else:
            print("Please enter a valid choice.")
    return choice

def createTable():
    db_name = "restaurant.db"
    create_table(db_name,table_name, sql)

def addProduct():
    print("Works")

def editProduct():
    print("Works")

def deleteProduct():
    print("Works")

def searchProduct():
    print("Works")


if __name__ == "__main__":
    display_menu()
    choice = select_option()
    Finished = False
    while not Finished:
        if choice == 1:
            createTable()
        elif choice == 2:
            addProduct()
        elif choice == 3:
            editProduct()
        elif choice == 4:
            deleteProduct()
        elif choice == 5:
            searchProduct()
        elif choice == 0:
            Finished = True
    
