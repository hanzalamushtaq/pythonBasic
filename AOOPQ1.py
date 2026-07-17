#Question 01: ATM Security Check (Private Attribute)
#Ek banking portal mein aapne security ke liye 
# __balance ko private variable banaya hai. Agar koi junior
#developer bahar se direct customer_account.__balance 
# likh kar value change karne ki koshish
#karega, toh Python kya error dega aur kyun?

class Account:
    __balance = 0
    def __init__(self, balance):
        self.__balance = balance
    def showBalance(self):
        return self.__balance
        
ac1 = Account(1000)
ac1.__balance = 2000
#Technically, this will not raise an error, but it will not change the private attribute __balance. Instead, it will create a new attribute __balance in the instance ac1. The original private attribute __balance remains unchanged.  
print(ac1.showBalance())
