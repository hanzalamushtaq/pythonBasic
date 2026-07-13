#Question 16: Notification Skipper
#1 se 10 tak user IDs ko for loop se traverse karein. 
#Jab ID 5 aaye (jo banned user hai), toh continue
#statement ka istemal kar ke usay skip kar dein aur baki IDs par notification bhejein

for i in range(1,6):
    if i==5:
        continue
    print(f"Notification send to {i}")