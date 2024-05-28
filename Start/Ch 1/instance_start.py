# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    _umar = "This is a static attribute."

    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute."
        self._umar = "Static attribute is changed."

    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount / 100)
        else:
            return self.price
    
    def setDiscount(self, percentage):
        self._discount = percentage

# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.99)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print(b1.getPrice())

# TODO: try setting the discount
print(f'Book2 original price = {b2.getPrice()}')
b2.setDiscount(25)
print(f'Book2 discounted price = {b2.getPrice()}')

# TODO: properties with double underscores are hidden by the interpreter
print(b2._Book__secret)
print(b2._umar)
print(Book._umar)

Book._umar = "Changing the class-wide static attribute."
print(Book._umar)

b3 = Book("The One Thing", "Umar Choudhry", 456, 49.95)
print(b3._umar)