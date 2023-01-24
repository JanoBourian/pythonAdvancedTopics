from .Device import Device

class Printer(Device):
    def __init__(self, name:str, connected_by:str, capacity:int):
        super().__init__(name, connected_by)
        self.capacity = capacity 
        self.remaining_pages = capacity
    
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages:int) -> None:
        if not self.connected:
            print(f"Your {self.name} is not connected!")
        else: 
            pages_press = self.remaining_pages - pages
            if  pages_press >= 0:
                print(f"Printing {pages} pages...") 
                self.remaining_pages -= pages
            else: 
                print(f"You need add {-pages_press} pages to continue...")
            