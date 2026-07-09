
#Password Check: Aik variable mein stored_password rakhen. 
# User se password input lein aur if statement se check karein
# ke dono match karte hain ya nahi
pswrd="Hello123"

user=input("Enter Password: ")

if pswrd==user:
    print("Access granted!")
else:
    print("Access denied!")