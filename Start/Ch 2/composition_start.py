# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def numTotalPages(self):
        totalPages = 0
        for ch in self.chapters:
            totalPages += ch.pages

        return totalPages

class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class Chapter:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages


b1 = Book("War and Peace", 39.0, Author("Leo", "Tolstoy"))

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.title)
print(b1.author)
print(b1.numTotalPages())
