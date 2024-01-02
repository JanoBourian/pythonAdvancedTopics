## Encapsulation

class TopSecretValues:
    
    def __init__(self,name:str, secure_name:str):
        self.name = name
        self.__secure_name = secure_name
    
    def print_key(self):
        print(self.__only_function_access())
        return self.__secure_name
    
    def __only_function_access(self):
        print("Super Secret Procedure")

value = TopSecretValues("random", "SHA256")
print(value.name)

# print(value.__secure_name)
# print(value.__only_function_access)
print(value.print_key())


## Composition

class Person:
    
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