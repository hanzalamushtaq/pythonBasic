#Question 05: School Database (Class vs Instance Variable)
#Aapko ek school management portal design karna hai. 
# Portal mein har student ka apna name aur 
#roll_number hai, lekin sab ka 
# school_name = "Future Academy" bilkul same hai. Memory
#bachaane ke liye aap school_name ko 
# class ke andar kahan aur kis variable ke tor par define
#karenge?

class Student:
    school_name = "Future Academy"

    def __init__(self, name, roll_number):
        self.name = name  
        self.roll_number = roll_number 
    def display_info(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}, School Name: {Student.school_name}")    
s1=Student("Ali", 101)
s2=Student("Ayesha", 102)
s1.display_info()
s2.display_info()
print(Student.school_name)