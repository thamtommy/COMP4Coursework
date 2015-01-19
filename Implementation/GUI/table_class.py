class Table:
    """A table class"""

    #constructor
    def __init__(self,table_number, date, time, number_of_people):
        self._table_number = table_number
        self._date = date
        self._time = time
        self._number_of_people = number_of_people
        self._order_list = []
        


    def get_table_number(self,table_number):
        self._table_number = table_number

    def get_date(self,date):
        self._date = date

    def get_time(self,time):
        self._time = time

    def get_number_of_people(self,number_of_people):
        self._number_of_people = number_of_people

    def create_order_list(self):
        item_list = []
        quantity_list = []
        self._order_list = [item_list,quantity_list]

    def manage_order_list(self):
        valid_item = False
        while not valid_item:
            item = input("Enter item: ")

            if len(item)>0:
                valid_item = True
                item_list.append(item)
        quantity_list.append(1)

    def display_order_list(self):
        print(self._order_list[0])
        print(self._order_list[1])
        
def main():
    Table_1 = Table(1,"19/01/2015","12:05",6)
    self.manage_order_list()
    self.display_order_list()
    
if __name__ == "__main__":
    main()
    
        
