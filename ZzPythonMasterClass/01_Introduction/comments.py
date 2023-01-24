# -*- coding: utf-8 -*-
'''A module-level docstring

Notice the comment above the docstring specifying the encoding.
Docstrings do appear in the bytecode, so you can access this through
the ``__doc__`` attribute. This is also what you'll see if you call
help() on a module or any other Python object.
'''
if __name__ == "__main__":
    import doctest
    doctest.testmod()


def my_function(a, b) -> float:
    """Return a float

    pow(a,b) = a**b = a^b

    Test

    python3 -m doctest -v comments.py

    >>> my_function(3,2)
    9

    >>> my_function(2,2)
    4
    """
    return a**b


#value = my_function(3, 2)
# print(value)

# help()
# help(my_function)
