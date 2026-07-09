#Slicing Expert: Aik list mein 6 fruits ke naam rakhen. 
# Slicing ka istemal karke sirf beech wale 3 fruits print karei

fruit=["Apple","Banana","Cherry","Watermelon","Melon","Mango"]

sliced=fruit[2:5]
print(sliced)

#Priority Task: Aik list banayein. .insert() method 
# ka istemal karte hue index 0 par aik naya urgent task add karein
sliced.insert(0,"Orange")
print(sliced)

#Remove Item: Aik product list se kisi specific item ko uske naam ke
# zariye .remove() karein
sliced.remove("Melon")
print(sliced)

#Pop Task: Aik list se aakhri item ko .pop() 
# karein aur print karein ke kaunsa item remove hua hai
print(fruit.pop())