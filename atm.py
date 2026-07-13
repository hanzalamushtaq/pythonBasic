#ATM Mockup: Aik balance variable rakhen. 
# User se withdraw amount lein. Agar amount balance se kam 
# ya barabar ho to "Success" print karein, 
# warna "Insufficient Balance"

volume=100000

amt=int(input("Enter amount to withdraw moeny: "))

if amt>=volume:
    print("Amount withdraw successfully!")
else:
    print("Insufficient Balance!")