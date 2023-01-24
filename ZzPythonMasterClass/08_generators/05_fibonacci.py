class Fibonacci:

    a = 0
    b = 1
    current = 0

    def __init__(self, positions):
        if positions < 2:
            raise ValueError("Input positions >= 2.")
        self.positions = positions

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 0:
            self.current += 1
            return self.a
        elif self.current == 1:
            self.current += 1
            return self.b
        elif self.current <= self.positions:
            self.current += 1
            aux = self.a + self.b
            self.a = self.b
            self.b = aux
            return aux
        raise StopIteration


fib = Fibonacci(20)
for i in fib:
    print(i, end=", ")
print(" ")
