from Classes.BookShelf import BookShelf
from Classes.Book import Book

book1 = Book("Harry Potter", 10)
book2 = Book("The Alchemyst", 20)
book3 = Book("Another Book", 500)

BS1 = BookShelf("Art", book1, book2)
print(BS1)
BS2 = BookShelf("Art", book3)
print(BS2)