#Category 3: Lists aur Mutability (Intermediate)
#Grocery List: Aik list banayein jis mein 3 items hon.
# User se chotha (4th) item input lein 
# aur use .append() ke zariye add karein

grocery=["Sugar","Tea","Ketchup"]

item=input("Add item to your grocery list: ")

grocery.append(item)
print(grocery)

#Length Checker: Aik list banayein aur
# .len() function ka istemal karte hue
# uski total items ki count print karein
print("Total items:",len(grocery))