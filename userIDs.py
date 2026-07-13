IDs={"user1":"user1001","user2":"user2002","user3":"user3003"}
user=input("Enter user name: ")
pswrd=input("Enter password: ")
if IDs[user]==pswrd:
    print("Access Granted!")
else:
    print("Username or Password is incorrect!")