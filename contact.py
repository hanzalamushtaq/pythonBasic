contact={"P1":"0301","P2":"0302","P3":"0303","P4":"0304"}
name=input("Enter name to search number: ")
if contact.get(name):
    print(contact[name])
else:
    print("Contact not found!")