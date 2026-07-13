#Question 09: Discount Calculator
#User se product ki price input lein, usay int mein 
#typecast karein, aur 10% discount minus kar ke final
#price print karein.

rate=int(input("Enter total price:"))
netTotal=rate-rate*0.1
print(f"Grand total:{rate}\nDics price:{rate*0.1}\nNet Total:{netTotal}")