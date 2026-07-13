#Question 21: Tweet Text Analyzer
#Ek function banayein jo ek string (jaise koi tweet) input le. 
# For loop se string ke har character par
#traverse karein. Agar woh .isalpha() hai, toh
#Vowels aur Consonants ko alag alag count karein, aur
#dono (2 values) ek sath return karein.

def countType(text):
    v=0
    c=0
    
    for char in text:
        if char.isalpha():
            if char.upper() in "AEIOU":
                v+=1
            else:
                c+=1
    return v,c

v,c=countType("aaaaaaaabbb34")
print(v)
print(c)