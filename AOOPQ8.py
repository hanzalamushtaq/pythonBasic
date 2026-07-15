#Aapke HR system mein jab bhi naya employee register ho, 
# use auto-incremented ID (jaise 101, 102,103) milni chahiye. 
# Constructor ke andar class variable ko update karke unique identity dynamic tarike
#se kaise assign karenge?

class Employee:
    id = 100

    def __init__(self, name):
        self.name = name
        Employee.id += 1 
        self.employee_id = Employee.id
        
e1=Employee("Ali")
print(f"Employee ID: {e1.employee_id}")
e2=Employee("Ayesha")
print(f"Employee ID: {e2.employee_id}")