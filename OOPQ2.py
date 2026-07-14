#Question 02: User Session Manager (Instance Attributes)
#Ek system user profile ke liye User class banayein. 
# Har user ka apna username aur status =
#"Active" hona chahiye. Ek naya user 
# object banayein aur uska status print karein.

class User:
    status="Active"
    def __init__(self,username):
        self.username=username
    def get_status(self):
        return self.status
    
u=User("JohnDoe")
print(u.get_status())