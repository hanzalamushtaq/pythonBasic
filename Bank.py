# Bank App project using OOP concepts
class Employee():
    __ID = 1000
    def __init__(self, name, age,address):
        self.name = name
        self.age = age
        Employee.__ID += 1
        self.employee_id = Employee.__ID
        self.address = address
class Address():
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
#Manager can create/remove edit account details

class Manager(Employee):
    def __init__(self, name, age,salary,address):
        super().__init__(name, age,address)
        self.salary = salary
        self.employee_id = Employee.__ID
    def create_account(self, account):
        self.account = account
class cashier(Employee):
    def __init__(self, name, age,salary,address):
        super().__init__(name, age,address)
        self.salary = salary
        self.employee_id = Employee.__ID
        
        