class Factorial:
    
    def __init__(self, number:int = 0):
        self.iterations = 0
        self.result = 1
        self.number = number
        self.max = number
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterations <= self.max:
            self.result = self.number * self.result
            self.number -= 1
            self.iterations += 1
            return self.result
        raise StopIteration
    
values = Factorial(0)
for i in values:
    print(i)

print("*****")
values = Factorial(4)
for i in values:
    print(i)

print("*****")
values = Factorial(10)
for i in values:
    print(i)