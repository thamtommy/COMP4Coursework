
class Table:
    """A table class"""

    #constructor
    def __init__(self,table_number, date, time, number_of_people):
        self._table_number = table_number
        self._date = date
        self._time = time
        self._number_of_people = number_of_people
        self._item_list = []
        self._quantity_list = []
        self._order_list = [self._item_list,self._quantity_list] 
        


    def get_table_number(self,table_number):
        self._table_number = table_number

    def get_date(self,date):
        self._date = date

    def get_time(self,time):
        self._time = time

    def get_number_of_people(self,number_of_people):
        self._number_of_people = number_of_people

    def add_item_to_order(self):
        valid_item = False 
        while not valid_item:
            item = input("Enter item: ")

            if len(item)>0:
                valid_item = True
                self._item_list.append(item)
        self._quantity_list.append(1)

    def display_order_list(self):
        print(self._order_list[0])
        print(self._order_list[1])

    def report_status(self):
        print("Table Number : {0}".format(self._table_number))
        print("Date Of Arrival : {0}".format(self._date))
        print("Time Of Arrival : {0}".format(self._time))
        print("Number Of People : {0}".format(self._number_of_people))
        print(self._order_list)



    
def main():
    Table_1 = Table(1,"19/01/2015","12:05",6)
    Table_1.add_item_to_order()
    Table_1.report_status()
    
if __name__ == "__main__":
    main()
    
        
