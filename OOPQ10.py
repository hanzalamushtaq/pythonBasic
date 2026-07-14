#Question 10: Banned User Filter (System Logic)
#Ek Profile class banayein. Ek method 
# restrict_access() likhein jo user ka status "Banned" set
#kar de taake system use block kar sake

class profile:
    def __init__(self):
        self.status = "Active"
    
    def restrict_access(self):
        self.status = "Banned"
        
u1=profile()
print(u1.status)
u1.restrict_access()
print(u1.status)