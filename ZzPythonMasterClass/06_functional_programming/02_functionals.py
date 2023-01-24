from functools import reduce
from math import ceil, sqrt, floor
# map, filter, reduces and map

# Example of map()


def square(item):
    return item**2


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(list(map(square, data)))

# Example of filter()

"""
List of odd prime numbers
(Remember what two is a even prime number)
"""


def check_prime(num):
    # No negative prime numbers
    if num <= 1:
        return False

    for i in range(2, ceil(sqrt(num))+1):
        if num % i == 0:
            return False
    return True


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
        12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

print(list(filter(check_prime, data)))

# Output
# [3, 5, 7, 11, 13, 17, 19]


# Example of zip() (Databases)

numbers = [1, 2, 3]
data = ['A', 'B', 'C']
print(list(zip(numbers, data)))

# Example of reduce()


def recursive_function(acc, item):
    if item == 0:
        return acc*1
    else:
        return item*acc


def factorial(num):
    items = [i for i in range(num + 1)]
    items.reverse()
    return reduce(recursive_function, items, 1)


for i in range(21):
    print(factorial(i))
