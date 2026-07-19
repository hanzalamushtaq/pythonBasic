#Vehicle
class Vehicle:
    def __init__(self,brand,price,model):
        self.brand=brand
        self.price=price
        self.model=model
    def tax(self):
        return "This is parent Class!" 
    
class gasCar(Vehicle):
    def __init__(self,brand,price,model):
        super().__init__(brand,price,model)
        
    def tax(self):
        return f"Tax: {self.price*0.15}"
class ElectricCar(Vehicle):
    def __init__(self,brand,price,model):
        super().__init__(brand,price,model)
    def tax(self):
        return f"Tax: {0}"
    
c1=gasCar("Honda",1000000,"Civic")
c2=ElectricCar("Tesla",9500000,"Model S")
cars=[]
cars.append(c1)
cars.append(c2)
for car in cars:
    print(car.tax())
        