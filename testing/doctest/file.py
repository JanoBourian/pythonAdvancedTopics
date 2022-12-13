""" 
This in the general information about the module

This module supplies one function called add(a,b). For example,

>>> add(2,3)
5
"""
from typing import Union
import doctest

def add(a:Union[int, float], b:Union[int,float]) -> Union[int,float]:
    """Return the sum of the two numbers together

    Args:
        a (Union[int, float]): First number
        b (Union[int,float]): Second numbers

    Returns:
        Union[int,float]: Sum of the two numbers
        
    >>> add(2,5)
    7
    >>> add(3.0, 5)
    8.0
    >>> add(3, "hello")
    TypeError: unsopported operand type(s) for +: 'int' and 'str'
    >>> add("hello", "message")
    'hellomessage'
    """
    try:
        return a + b
    except TypeError:
        print("TypeError: unsopported operand type(s) for +: 'int' and 'str'")
    except Exception as e:
        print("Invalid Operation")

if __name__ == '__main__':
    doctest.testmod()