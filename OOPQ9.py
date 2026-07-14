#Question 09: Hotel Booking System (State Mutation)
#Ek HotelRoom class banayein jismein 
#is_occupied = True ho. Ek method checkout() banayein
#jo is value ko update karke False kar de.

class room:
    def __init__(self):
        self.is_occupied = True

    def checkout(self):
        self.is_occupied = False
        
r1=room()
print(r1.is_occupied)
r1.checkout()
print(r1.is_occupied)