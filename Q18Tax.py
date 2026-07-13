#Question 18: Automated Tax Billing
#Ek function calculate_bill(price, tax=5) banayein 
# jahan tax ki default value 5 ho. Function
#mein total bill return karein. Ek bar tax pass kar ke
# aur ek bar bina tax pass kiye function call karein

def calculateBill(price,tax=5):
    return price+tax

print(calculateBill(100,10))