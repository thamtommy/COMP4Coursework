
# this provides a friendly interface when adding an item to an order (radio button)
    def DrinkorDish(self): 
        self.hello_radio_button = RadioButtonWidget("Item type","Please select an item type",("Drink","Dish"))
        self.instantiate_button = QPushButton("Add")
        
        self.initial_layout = QGridLayout()
        self.initial_layout.addWidget(self.hello_radio_button)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_widget = QWidget()
        self.select_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.select_widget)
