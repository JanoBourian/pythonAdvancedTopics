## Create our own iterator in a class

class NewPow:
    
    def __init__(self, max:int = 0, exponent:int = 0):
        self.max = max
        self.exponent = exponent
        self._number = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._number <= self.max:
            result = self._number ** self.exponent
            self._number += 1
            return  result
        raise StopIteration
    
    def __repr__(self):
        return f"< NewPow {self.max} - {self.exponent}>"

iterable = NewPow(99, 100)

for i in iterable:
    print(i)