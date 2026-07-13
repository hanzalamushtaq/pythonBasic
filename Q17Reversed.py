#Question 17: Space Rocket Countdown
#Ek while loop banayein jo user se number le 
#aur wahan se 0 tak ulta (reverse) count down print kare.

num=int(input("Enter a number: "))

for i in reversed(range(0,num+1)):
    print(i)