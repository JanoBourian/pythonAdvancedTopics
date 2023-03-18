class Fibo:
    
    def __init__(self, number:int = 0):
        self.number = number
        self.iterations = 0
        self.a = 0
        self.b = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterations == 0:
            self.iterations += 1
            return self.a
        
        if self.iterations == 1:
            self.iterations += 1
            return self.b
        
        if self.iterations <= self.number + 2:
            self.a, self.b = self.b, self.a + self.b
            self.iterations += 1
            return self.b
        
        raise StopIteration
    
iterable = Fibo(0)

for i in iterable:
    print(i)