class Book:
    TYPE = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.TYPE[0], weight + 100)
    
    @classmethod
    def paperback(cls, name, weight):
        return cls(name, cls.TYPE[1], weight + 100)

print(Book.TYPE)
book = Book("Harry potter", "hardcover", 1500)
book2 = Book.hardcover("Alquimista", 100)
book3 = Book.paperback("Attack of monsters", 1000)

print(book)
print(f'book2: {book2}')
print(f'book3: {book3}')