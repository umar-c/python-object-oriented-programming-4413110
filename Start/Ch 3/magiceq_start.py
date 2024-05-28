# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Book):
            raise ValueError("Oops, can't copmare an object of type Book to a non-Book object!")
                             
        if (self.title == value.title) and (self.author == value.author) and (self.price == value.price):
            return True
        else:
            return False

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Oops, can't copmare an object of type Book to a non-Book object!")
        
        return (self.price >= value.price)

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Oops, can't copmare an object of type Book to a non-Book object!")
        
        return (self.price < value.price)

b1 = Book("War and Peace", "Leo Tolstoy", 39.96)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace vol.2", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)
b5 = object()

# TODO: Check for equality
print(f'b1 == b2: {b1 == b2}')
print(f'b1 == b3: {b1 == b3}')
#print(f'b1 == b5: {b1 == b5}')

# TODO: Check for greater and lesser value
print(f'b2 >= b1: {b2 >= b1}')
print(f'b3 >= b1: {b3 >= b1}')
print(f'b3 < b1: {b3 < b1}')

# TODO: Now we can sort them too
books = [b3, b2, b1, b4]
books.sort()
print(f'Sorted books: {[book.title for book in books]}')