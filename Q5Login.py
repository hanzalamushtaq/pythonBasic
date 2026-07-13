#Question 05: Security Login Lockout
#Ek while loop ka istemal karein jo 1 se 3 tak "Login Attempt X" print kare
# taake 3 attempts ke baad
#system lock hone ka logic banaya ja sake.

num=1
while num<=3:
    print(f"Login Attempt {num}")
    num+=1
print("System Locked!")