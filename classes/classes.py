## Simple class 

class Dog:
       
    def __init__(self, name):
        self.name = name
        self.kind = "canine"
        self.tricks = []
        
    def __repr__(self):
        return self.__private_method()
    
    def __private_method(self):
        return f"<Dog> Name: {self.name}. Kind: {self.kind}"

fido = Dog("Fido")
print(fido)
print(fido.name)
print(fido.kind)