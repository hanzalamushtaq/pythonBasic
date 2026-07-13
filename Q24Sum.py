#Question 24: Multi-Step Math Engine
#Ek function banayein jo ek parameter n le. Function ke
#andar (local variables use karte hue) ek while
#loop chalayein jo 1 se lekar n tak tamam 
#natural numbers ko aapas mein plus (sum) kare aur aakhir
#mein total sum return kare.
def sumNaturals(n):
    i=1
    sum=0
    while i<=n:
        sum+=i
        i+=1
    return sum

print(sumNaturals(10))