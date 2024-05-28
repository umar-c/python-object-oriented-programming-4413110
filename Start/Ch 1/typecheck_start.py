# Python Object Oriented Programming by Joe Marini course example
# Checking class types and instances


class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# TODO: use type() to inspect the object type
print(type(b1))
print(type(n1))

# TODO: compare two types together
print(f'type(b1) == type(b2) = {type(b1) == type(b2)}')
print(f'type(b1) == type(n2) = {type(b1) == type(n2)}')

# TODO: use isinstance to compare a specific instance to a known type
print(f'isinstance(b1, Book) = {isinstance(b1, Book)}')
print(f'isinstance(b2, Book) = {isinstance(b2, Book)}')
print(f'isinstance(n1, Book) = {isinstance(n1, Book)}')
print(f'isinstance(b1, Newspaper) = {isinstance(b1, Newspaper)}')
print(f'isinstance(n2, Object) = {isinstance(n2, object)}')