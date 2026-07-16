#Ek cloud backend script mein aapko Fahrenheit se Celsius 
# temperature convert karne ke liye ek tool
#chahiye jise chalane ke liye kisi object (self)
# ki zaroorat nahi hai. @staticmethod decorator ka use
#karke is conversion method ka basic structure banayein.

class Temperature:
    @staticmethod
    def FtoC(f):
        c = (f - 32) * 5/9
        return c
    
temp = Temperature()
celsius = temp.FtoC(100)

print(Temperature.FtoC(100))
print(f"100°F is equal to {celsius:.2f}°C")