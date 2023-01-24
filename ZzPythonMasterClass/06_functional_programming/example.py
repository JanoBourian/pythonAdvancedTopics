"""
Time to execute of functional programming
with decorators
"""

from time import time

data = [i for i in range(99999)]


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


start = time()
multiply_by2(data)
print(f"Elapsed time {time() - start }\n")
# Output
# Elapsed time 0.0011849403381347656

start = time()
list(map(lambda x: x*2, data))
print(f"Elapsed time {time() - start }\n")
# Output
# Elapsed time 0.00096893310546875
