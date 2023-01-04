from typing import Generator

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