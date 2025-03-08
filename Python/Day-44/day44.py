# Create a class for a book with attributes like title and author.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

book1 = Book("Encyclopedia", "Ram", 120)
book1.display_book()

title = input("Enter title : ")
author = input("Enter author : ")
price = int(input("Enter price : "))

book2 = Book(title, author, price)
book2.display_book()
