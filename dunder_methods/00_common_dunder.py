print(f"int {dir(int)}")

class NewInteger(int):
    def __init__(self, value:int):
        self.value = value
        
    def __add__(self, other):
        return self.value + other + 5 

new_integer = NewInteger(1)
new_value = new_integer.__add__(1)
print(f"Value {new_value}")

print(f"None {dir(None)}")

iterable = iter([4,5])
print(f"iterable {dir(iterable)}")
print(f"list {dir(list)}")