#Question 25: E-Commerce Discount Engine
#Ek list mein cart items ki prices di gayi hain.
#Ek for loop chalayein. Agar price 100 se upar hai, toh us
#par 10% discount apply kar ke print karein. 
#Agar koi price 0 aati hai (jaise free item), toh continue use
#kar ke us iteration ko skip kar dein.

cart=[100,900,89,890,770,80,250]
for i in cart:
    if i>=100:
        print(f"Total: {i-i*.1}")
    else:
        continue