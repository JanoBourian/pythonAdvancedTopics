from collections.abc import Iterable
from typing import Any

def find_value(iterable:Iterable, value:Any)->Any:
    iter_object = iter(iterable)
    index = 0
    while True:
        try:
            if(next(iter_object) == value):
                return index
            index += 1
        except StopIteration:
            break

iterable = ["a", 1, 2, "c", "d", "e", "f", "g", "h", "4", 5, 7]
index = find_value(iterable, "w")
print(index)