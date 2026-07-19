class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_limit(self):
        return 0 

class Student(Member):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__Limit = 5

    # Method Overriding
    def get_limit(self):
        return self.__Limit

class Teacher(Member):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__Limit = 10

    # Method Overriding
    def get_limit(self):
        return self.__Limit


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__isAvailable = True

    def Availability(self):
        return self.__isAvailable

    def Issue(self):
        if self.__isAvailable:
            self.__isAvailable = False
            return True
        else:
            return False

    def returnBook(self):
        self.__isAvailable = True


class Library:
    def __init__(self):
        self.__books = []
        self.__borrowed_books = {} 
        
    def add_book(self, book):
        if isinstance(book, Book):
            self.__books.append(book)
        
    def issueBook(self, book, member):
        if isinstance(book, Book) and isinstance(member, Member):
            if book in self.__books:
                if not book.Availability():
                    return "Out of Stock"
                
                if member not in self.__borrowed_books:
                    self.__borrowed_books[member] = []
                
                if len(self.__borrowed_books[member]) >= member.get_limit():
                    return "Borrowing Limit Exceeded"
                
                if book.Issue():
                    self.__borrowed_books[member].append(book)
                    return "Book Issued"
            else:
                return "This book does not belong to this library."
        return "Invalid Book or Member Object"


lib = Library()
b1 = Book("Python Basics", "John Doe")
b2 = Book("Data Structures", "Jane Doe")
    
lib.add_book(b1)
lib.add_book(b2)
st1 = Student("Zain", 20)
print(f"Attempt 1: {lib.issueBook(b1, st1)}")  
print(f"Attempt 2: {lib.issueBook(b1, st1)}")  