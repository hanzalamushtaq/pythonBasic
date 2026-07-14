#Ek SmartBulb class banayein jismein ek attribute 
# state = "OFF" ho. Isme ek method turn_on()
#banayein jo state ko "ON" kar de.


class Bulb:
    status = "OFF"
    def __init__(self):
        pass
    def turnOn(self):
        self.status = "ON"
    def get_status(self):
        return self.status
    
b1=Bulb()
b1.turnOn()
print(b1.get_status())