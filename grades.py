#Smart Grading: Student ke marks (0-100) input lein. 
# 90+ par "Grade A", 80-89 par "Grade B", aur baki par "Grade C" 
# print karein

m=int(input("Enter your marks(0-100): "))
if m in range(0,101):
    if m>=90:
        print("You got A")
    elif m>=80:
        print("You got B")
    else:
        print("you got C")
else:
    if m>0:
        print("Incorrect marks!")
    else:
        print("you entered negative number!")