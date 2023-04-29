'''
Single responsability principle
A class should have ONNE responsability and no more
'''
import os 

class Books:
    def __init__(self):
        self.list_books = {}
        self.number = 0
    
    def add_book(self, book) -> None:
        self.number += 1
        self.list_books[self.number] = book
        
    def __repr__(self):
        return f"< BOOKS: {str(self.list_books)}>"
    
class SaveBooks:
    
    @staticmethod
    def save_books(filename:str, books:Books) -> None:
        curr_path = os.path.abspath(os.path.dirname(__file__))
        directory = os.path.join(curr_path, filename)
        with open(directory, 'w') as f:
            f.write(str(books))
    
b = Books()
b.add_book("Book A")
b.add_book("Book B")
print(f"{b}")

s = SaveBooks()
s.save_books("my_cur_books", b)