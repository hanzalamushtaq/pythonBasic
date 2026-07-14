#Question 07: Database Connection Setup (Tuple Usage)
#Ek DatabaseConfig class banayein jismein host aur port ko aik tuple attribute credentials =
#("localhost", 3306) mein store kiya jaye taake credentials immutable rahin.

class DBConfigure:
    def __init__(self, address, port):
        self.credentials = (address,port)
        
    def show(self):
        return self.credentials
    
sq=DBConfigure("localhost", 3306)
print(sq.show())