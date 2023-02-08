from random import randint

def my_generator(n:int = 0):
    value = 0
    while value < n:
        yield value
        value += 1

## Check the methods inside
gen = my_generator(3)
print(dir(gen))

## Create a list based on generator
gen_2 = my_generator(10)
list_results = (i*i for i in gen_2)
print(list(list_results))

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