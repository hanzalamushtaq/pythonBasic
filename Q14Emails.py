#Question 14: Customer Data Cleaning
#Ek system mein duplicate email IDs list mein aagayi hain.
#Us list ko pehle set mein convert karein taake
#duplicates uṛ jayen, phir .add() use kar ke ek naya email add karein aur print karein.

mails=["example1@gmail.com",
       "example2@gmail.com",
       "example2@gmail.com",
       "example3@gmail.com",
       "example1@gmail.com",
       "example4@gmail.com"]
clean=set()
for i in mails:
    clean.add(i)
    
print(clean)