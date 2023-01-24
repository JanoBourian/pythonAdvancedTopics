""" 
This is a functions
"""


def is_man() -> None:
    """
    def is_man() -> None
    """
    print("is a man.")


is_man()


def is_even(number) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


for i in range(10):
    print(is_even(i))


def new_user(name, last_name, age, /, games, *, nickname):
    print(f"""
    name: {name}
    last_name: {last_name}
    age: {age}
    games: {games}
    nickname: {nickname}
    """)


new_user('frank', 'muniz', 38, games=['javascript',
                                      'python'], nickname='janobourian')

new_user('andrei', 'robles', 31, games=['javascript',
                                        'python'], nickname='janobourian')


def suma(num1, num2) -> float:
    return num1 + num2


result = suma(2, 3)

print(f"The answer is: {result}")

# *args and **kwargs


def super_function(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args)


print(super_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, num1=5, num2=10))


# Example to CarbonApp and <super> docstring. :D

def largest_even(number_list) -> float:
    """
    This function receives a list of numbers 
    and return the largest even value.

    Parameters
    ----------
    number_list : list
        list of numbers

    Returns 
    ----------
    float
        the largest even value
    """

    evens = []
    for i in number_list:
        if i % 2 == 0 and i not in evens:
            evens.append(i)
    return max(evens)


print(largest_even([10, 2, 3, 4, 8, 11]))


# Walrus Operator :=  (3.8.* or superior)

a = 'mathus'

if (n := len(a)) < 10:
    print(f"Too long {n} elements")

# Output: Too long 6 elements

# Walrus Operator in a while expression

while ((n := len(a)) > 0):
    print(a[n-1], end="")
    a = a[:-1]

# Output: suhtam


# SCOPE - what variables do I have access to?

# 1.- start with local
# 2.- Parent local?
# 3.- Blobal
# 4.- Built in functions

a = 1


def parent():
    a = 10

    def confusion():
        return a
    return confusion()


print(parent())
print(a)

# global Keyword

total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())
print(total)


# nonlocal

def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print("inner: ", x)
    inner()
    print("outer: ", x)


outer()
