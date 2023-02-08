# Looping

This file was created to learn about the different ways to create efficient looping but focused in some important topics:
- Iterable/Iterator
- Generator
- Coroutines
- Thread/Threading
- Async operations

## Iterator

An iterator has two important methods:

```python
__iter__()
__next__()
```

For more information please visit the next [link](https://www.w3schools.com/python/python_iterators.asp)

## Generator

Basiclly, generator is a function that returns an iterator that produces a sequence of values when iterated over.

```python
def generator_name(arg):
    # statements
    yield something
```

But, we have other application with *send()* statment:

```python
def counter(start = 0, limit = 10):
    value = start
    while value < limit:
        breakpoint()
        value += yield value
    yield value

gen_2 = counter(start = 0, limit = 100)
gen_2.send(None) # prime the generator
while True:
    try:
        value = randint(1, 3)
        total = gen_2.send(value)
        print(f"sent: {value}, got {total}")
    except StopIteration:
        print("Ends")
        break
```

For more information please visit the next [link](https://www.iditect.com/guide/python/class-member-generator-send-close-throw.html)

## Coroutines

Coroutines have a little difference of Generators cause *Generators* produce data to consume but *Coroutines* consume data.

First source of information is [here](https://www.geeksforgeeks.org/coroutine-in-python/)

## Thread

## Async operations