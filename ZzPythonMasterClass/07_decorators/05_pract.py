from time import time

# Decorators


def performance(name):
    def wrapper(func):
        def wrapper2(*args, **kwargs):
            t1 = time()
            n = func(*args, **kwargs)
            t2 = time()
            print(f' {name} in {t2-t1} to {n} operations.')
        return wrapper2
    return wrapper


@performance('Function')
def gen(n):
    total = 0
    for i in range(n):
        total += i
    return n


gen(999999999)
