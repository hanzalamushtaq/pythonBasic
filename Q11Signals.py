#Question 11: Traffic Light Controller
#Ek if-elif-else block banayein jo user input ("Red", "Yellow", "Green") ke 
# mutabiq instructions print
#kare: Red par "Stop", Yellow par "Slow Down", Green par "Go".

user=input("Enter Signal state(Red,Green,Yellow): ")

if user.upper()=="RED":
    print("Stop!")
elif user.upper()=="GREEN":
    print("Go!")
else:
    print("Slow Down!")