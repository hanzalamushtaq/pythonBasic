bal=5000
wth=int(input("Enter withdraw amount: "))

if wth<=bal:
    print(f"Withdraw amount: {wth}\n Remianing balance: {bal-wth}")
else:
    print("Insufficient Funds!")