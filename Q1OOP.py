class Account:
    __balance=0
    def __init__(self,name,bal):
        self.__balance=bal
        self.name=name
    #getter to get balance
    def get_balance(self):
        return self.__balance
    #setter to set balance
    def set_balance(self,bal):
        if type(bal)!=str:
            if bal>=0:
                self.__balance=bal
            else:
                print("Balance cannot be negative")
        else:
            print("Invalid balance amount")
    def accoutDetails(self):
        print("Account holder name:",self.name)
        print("Account balance:",self.__balance)
ac=Account("John Doe", 1000)
ac.set_balance(-112)
ac.accoutDetails()