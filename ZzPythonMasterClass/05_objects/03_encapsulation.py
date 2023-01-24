# Encapsulation
# Abstraction
# Herencia
# Polimorfismo

class Person:
    def __set_name(self, name):
        self.__name = name

    def __init__(self, name, age):
        self.__set_name(name)
        self.__age = age

    def get_name(self):
        return self.__name


user900221 = Person('Alexander', 40)
print(user900221.get_name())
# user900221.__set_name('Dunder') #Error
print(user900221.get_name())
user900221.__name = 'Emily'
print(user900221.get_name())
print(user900221.__name)  # Error
print(user900221.get_name())
