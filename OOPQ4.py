#Question 04: Digital Wallet System (Default Constructor)
#Ek Wallet class banayein. Jab bhi naya wallet object bane,
# __init__ constructor automatically
#chalna chahiye aur starting balance 0 set karna chahiye

class Wallet:
    balance = 0
    def __init__(self):
        self.balance = 0
    def show_balance(self):
        return self.balance
    
t1=Wallet()
print(t1.show_balance())

