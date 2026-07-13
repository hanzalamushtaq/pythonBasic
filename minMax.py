#Leaderboard Analysis: 5 students ke marks ki list banayein. 
# max() aur min() ka istemal karke highest aur lowest
# marks find karein

marks=[90,91,30,88,83]
print(min(marks))
print(max(marks))

#Data Correction: Aik list banayein `. Indexing ka istemal karte
# hue 30 ko `35 se replace karein (Mutability check)
marks[2]=35
print(min(marks))