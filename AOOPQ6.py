#Question 05: School Database (Class vs Instance Variable)
#Aapko ek school management portal design karna hai. 
# Portal mein har student ka apna name aur 
#roll_number hai, lekin sab ka 
# school_name = "Future Academy" bilkul same hai. Memory
#bachaane ke liye aap school_name ko class ke andar kahan 
# aur kis variable ke tor par define
#karenge?

class ride:
    count=0
    def __init__(self, name):
        self.name = name
        ride.count+=1
    
r1=ride("Ali")
r2=ride("Ayesha")
r3=ride("Ahmed")
print(ride.count)