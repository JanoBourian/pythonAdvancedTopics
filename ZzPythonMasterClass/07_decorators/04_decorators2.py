from time import time

# Decorators


def my_decorator(name):
    def wrapper(func):
        def wrapper2(*args, **kwargs):
            t1 = time()
            func(*args, **kwargs)
            t2 = time()
            print(f' {name} in {t2-t1}')
        return wrapper2
    return wrapper


@my_decorator('Function one')
def hello(greeting, emoji=';)'):
    print(greeting, emoji)


hello('Hiii')
