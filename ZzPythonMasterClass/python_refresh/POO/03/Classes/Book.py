class Book:
    def __init__(self, name:str, quantity:int):
        self.name = name
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.name} - {self.quantity}"
    
    def is_disponible(self):
        if self.quantity >0:
            print(self.__str__())
            return self.quantity
        else: 
            return 0
    