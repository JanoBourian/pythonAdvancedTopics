from .Book import Book

class BookShelf:

    def __init__(self, name:str,  *books:Book):
        self.books = []
        self.quantity = 500 
        self.name = name
        total_to_add = 0
        for i in range(len(books)):
            total_to_add += books[i].quantity
        
        if self.quantity - total_to_add < 0:
            raise Exception(f"Sorry, this BookShelf capacity is {self.quantity}")
        else: 
            self.add_books(*books)
    
    def __str__(self):
        return f"BookShelf name {self.name} whit {len(self.books)} books and {self.quantity} spaces."
    
    def add_books(self, *books):
        for item in books: 
            self.books.append(item)
            self.quantity -= item.quantity


