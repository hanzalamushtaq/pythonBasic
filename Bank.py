class BankAccount:
    __total = 0

    def __init__(self, owner, initial_deposit):
        self.owner = owner
        BankAccount.__total += 1
        self.__account_no = 1000 + BankAccount.__total
        self.__balance = self.__set_balance(initial_deposit)
        print(f"Account created Successfully!\nAccount holder: {self.owner} \nAccount number: {self.__account_no} \nInitial balance: {self.__balance}")
        print("\n")
    # setter for balance
    def __set_balance(self, amount):
        if amount>=0 and amount!=str:

            return amount
        else:
            print("Error: Invalid balance amount.")
            return 0
    # Getter for balance
    def get_balance(self):
        return self.__balance
    # Secure Deposit
    def set_deposit(self, amount):
        if self.__set_balance(amount) > 0:
            self.__balance += self.__set_balance(amount)
            print(f"Deposit of {amount} successful.\nNew balance: {self.__balance}")
    # Secure Withdrawal Method
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Error: Insufficient funds.")
        else:
            self.__balance -= self.__set_balance(amount)
            print(f"Withdrawal of {amount} successful.\nNew balance: {self.__balance}")
    @staticmethod
    def get_total_accounts():
        return BankAccount.__total
    
    
ac=BankAccount("John Doe", 500)
ac.set_deposit(200)
ac.withdraw(100)
ac2=BankAccount("Jane Smith", 1000)
ac3=BankAccount("Alice Johnson", 1500)
print(f"Total accounts created: {BankAccount.get_total_accounts()}")