## breakpoint() use

from dataclasses import dataclass

@dataclass
class Information:
    mesagge: str
    available_days: int

x = Information("Hello my friend", 15)
# breakpoint()
x.mesagge
# breakpoint()
x.available_days

## callable

array = [1, 2, 3]
function = lambda x: x + 1
print(f"Function {callable(function)}")
print(f"Array: {callable(array)}")

## chr
for _ in range(0, 128):
    print(chr(_))
    
## classmethod / staticmethod / property

## dir()

class PersonalClass:
    
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress
    
    def __dir__(self):
        return ["name"]

p = PersonalClass("james", 18, "St. Petesburgh")
print(dir(p))
print(p.age)

## Enumerate

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

value = enumerate([1,2,3], 0)
print(next(value))
print(next(value))
print(next(value))
