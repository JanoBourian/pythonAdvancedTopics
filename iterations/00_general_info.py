"""
Iterator Types:

container.__iter__()
iterator.__iter__()
iterator.__next__()
containers: lists, tuples, dictionaries, and sets
"""

# If you want to use a container mode
cont = [0, 1, 2, 3, 4]
alfa = cont.__iter__()
# print(next(alfa))
# print(next(alfa))
# print(next(alfa))
# print(next(alfa))
# print(next(alfa))
# print(next(alfa))

# A complete class

class Iterable:
    def __init__(self):
        self.max = 10
        self.counter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.max:
            self.counter += 1
            return self.counter
        raise StopIteration
    
inst = Iterable()
for i in inst:
    print(i)