#Ek list mein blog tags hain: ["tech", "python", "tech"]. Is list ko
# set mein convert karein taake
#duplicate "tech" khatam ho jaye, aur unique tags print karein.
tags=["tech","python","tech"]
sort=set()

for i in tags:
    sort.add(i)
print(sort)