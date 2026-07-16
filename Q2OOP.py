from ast import Add


class Address:
    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state
        
class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    def ShippingLabel(self):
        print("Customer name:",self.name)
        print("State:",self.address.state)
        print("City:",self.address.city)
        print("Pincode:",self.address.pincode)
ad=Address("Vehari","61100","Punjab")
c=Customer("Ali","Male",ad)
c.ShippingLabel()