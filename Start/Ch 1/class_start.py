# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    def getBookList():
        if Book.__booklist is None:
            Book.__booklist = []
            
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, bookType):
        self.title = title
        if bookType in Book.BOOK_TYPES:
            self.bookType = bookType
        else:
            raise ValueError(f'{bookType} is not a vlaid book type!')


# TODO: access the class attribute
print("Book Types:", Book.getBookTypes())

# TODO: Create some book instances
b1 = Book("First Book", Book.BOOK_TYPES[0])
b2 = Book("Second Book", "EBOOK")

# TODO: Use the static method to access a singleton object
theBooks = Book.getBookList()
print(theBooks)

# Backdoor to access the secret properties
theBooks = b1._Book__booklist
print(theBooks)

theBooks.append(b1)
theBooks.append(b2)

print(theBooks)