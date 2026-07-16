#Aap ek smart home lock system bana rahe hain jahan 
# passcode __pin private hai. Ek aisa setter
#method set_pin(new_pin) likhein jo check kare ke agar 
# new_pin sirf numbers (digits) par mabni hai
#tabhi update kare, warna error message de.

class SmartLock:
    __pin = "1234"
    
    def set_pin(self, new_pin):
        if type(new_pin) == int:
            self.__pin = new_pin
            print("Pin updated successfully.")
        else:
            print("Error: Pin must be numeric.")

    def get_pin(self):
        return self.__pin
    
p1=SmartLock()
p1._SmartLock__pin = 2222
print(p1.get_pin()) 
#p1.set_pin(5678)    
