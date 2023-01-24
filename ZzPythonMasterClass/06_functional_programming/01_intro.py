"""
Time to execute of functional programming
with decorators
"""

from time import time

# Decorator


def test_time(name):
    def wrapper(function):
        def wrapper_2(*args, **kwargs):
            # Execute
            start = time()
            function(*args, **kwargs)
            end = time() - start
            print(f" {name} in {end} seconds\n")
        return wrapper_2
    return wrapper


data = [i for i in range(1000)]


@test_time("function")
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


multiply_by2(data)
