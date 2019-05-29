class Customer:
    __log = " "
    __password = " "

    def _init_(self, log, password):
        self.__log = log
        self.__password = password
        self.customer_details = []


    def showCustomer(self):
        description= (self.name+ " " + self.surname).title()
        print(description)

