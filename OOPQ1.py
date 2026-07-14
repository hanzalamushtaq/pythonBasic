#Question 01: E-Commerce Product Registry (Class & Object)
#Ek online store ke liye Product class banayein jismein
# name aur price ke default attributes hon. Is
#class ke do objects (e.g., Laptop aur Smartphone)
# instantiate karein aur dono ki details print karein.

class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def details(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price:.2f}")
        
laptop = product("Laptop", 75000)
smartphone = product("Smartphone", 30000)

laptop.details()
smartphone.details()