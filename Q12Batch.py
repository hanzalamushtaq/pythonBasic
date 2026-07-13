#Question 12: Odd/Even ID Batching
#Ek while loop 1 se 20 tak chalayein. Modulo operator % ka
#istemal karte hue check karein, agar ID
#even hai toh "Process Batch A", agar odd hai toh "Process Batch B" print karein.

i=1
while i<=20:
    if i%2==0:
        print(f"{i}: Process Batch A")
    else:
        print(f"{i}: Process Batch B")
    i+=1