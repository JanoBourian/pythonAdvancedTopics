from abc import ABC, abstractmethod

class Person(ABC):
    
    def __init__(self, age):
        self.age = age
    
    @abstractmethod
    def set_age(self, age):
        pass

class Citizen(Person):
    
    def __init__(self, age, name):
        self.name = name 
        super().__init__(age)
        
    def set_age(self, age):
        self.age = age
    
    def say_hello(self):
        print("Hello!")
    
person1 = Citizen(age = 5, name = "fernando")
person1.say_hello()
print(person1.age)
person1.set_age(15)
print(person1.age)