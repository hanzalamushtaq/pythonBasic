#Question 22: ATM Withdrawal Logic
#Ek balance = 10000 set karein. Ek while loop banayein 
#jo user se baar baar withdrawal amount
#pooche. Agar amount balance se zyada hai, 
#"Insufficient" print karein. Agar amount balance ke barabar
#ho jaye, balance 0 kar dein aur break statement
#ka istemal kar ke loop foran rok dein
balance=10000
while balance:
    amount=int(input("Enter withdraw balance: "))
    if amount<=balance:
        print(f"{amount} withdraw")
        balance-=amount
        print(f"{balance} remaining")
    elif balance==0:
        break
    else:
        print("Insuffecient Balance!")