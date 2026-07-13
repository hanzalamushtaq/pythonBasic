#Question 08: Immutable DB Credentials
#Database ka Host aur Port ek tuple mein store karein 
# aur code mein usay change karne ki koshish
#karein taake error aaye aur sabit ho ke credentials (tuples) safe hain.

dataBase=("Local Host",5001)
dataBase[1]=4001
