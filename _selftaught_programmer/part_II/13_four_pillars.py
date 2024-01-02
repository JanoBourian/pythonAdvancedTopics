## Composition

class Person():
    
    def __init__(self, name:str):
        self.name:str = name

class Pet:
    
    def __init__(self, name:str, breed:str, owner:Person):
        self.name: str = name
        self.breed: str = breed
        self.owner: Person = owner
        
mike = Person("mike")
milo = Pet("max", "mix", mike)
print(milo.owner.name)