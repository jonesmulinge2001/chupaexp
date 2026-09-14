# library system
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")
    
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"You have returned '{self.title}' by {self.author}.")
    
    def display_info(self):
        availability = "Available" if self.is_available else "Not Available"
        print(f"Title: {self.title}, Author: {self.author} is {availability}")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} by {book.author} has been added to the library.")
    
    def show_books(self):
        if not self.books:
            print("No books in the library now")
            return
        for book in self.books:
            book.display_info()
    
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        
        return None
    

# create a library instance
library = Library("Chuka University Library")

# create books
book1 = Book("Python Programming", "Nick K")
book2 = Book("Java Programming", "Samuel K")
book3 = Book("Web Development", "Jonathan Mulinge")

# add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# display all books
library.show_books()

# Borrow a book
print("\nBorrowing a book...")
book = library.find_book('Python Programming')
if book:
    book.borrow()

# display books again
library.show_books()

# return a book
print("\nReturning a book...")
book.return_book()

# diaplay books again
library.show_books()