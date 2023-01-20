from typing import Generator
from random import randint

def some_sequence(size:int = 0) -> Generator:
    num = 0
    while num < size:
        yield num
        num += 1

gen = some_sequence(10)

next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)

# Generator to evaluate information in a list
values = [0, 1, 2, 3, 4, 5, 6 , 7]

def check_value(iterable, number) -> int:
    it = iter(iterable)
    while True:
        try:
            if(next(it) == number):
                return number
        except StopIteration:
            break

value = check_value(values, 7)
print(value)

### Simple generator

def fib(count:int):
    a, b = 1, 0
    for _ in range(count):
        a, b = b, a + b
        yield b

gen = fib(10)
print(gen)
# while True:
#     print(next(gen))
    
### Other way to implement generators

def counter(start = 0, limit = 10):
    value = start
    while value < limit:
        value += yield value
    yield value

gen_2 = counter()
gen_2.send(None) # prime the generator
while True:
    value = randint(1, 3)
    total = gen_2.send(value)
    print(f"sent: {value}, got {total}")