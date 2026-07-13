#Question 23: Employee Registry System
#Ek khali dictionary employees = {} banayein. 
#for loop aur range(3) ka istemal karte hue user se 3
#dafa employee ka name aur salary input lein. 
#Name ko Key aur Salary ko Value bana kar dictionary
#mein add karein aur aakhir mein print karein.

employees={}
n=int(input("Number of employees:"))
for i in range(n):
    key=input("Enter your name: ")
    val=int(input("Enter your salary: "))
    employees[key]=val
print(employees)