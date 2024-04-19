import timeit

# Basic usage
print(timeit.timeit('"-".join(str(n) for n in range(100))', number = 10000))

# Using repeat
TIMES = 100000000
SETUP = """
symbols = '$¢£¥€¤'
"""
FOR_STATEMENT = """
final_list = []
for s in symbols:
    final_list.append(ord(s))
"""
print(timeit.repeat('[ord(s) for s in symbols]', setup=SETUP, number=TIMES))
print(timeit.repeat(FOR_STATEMENT, setup=SETUP, number=TIMES))

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *(f'{x:.3f}' for x in res))

print("")
print("Is list comprehension faster than 'for' statement?")
print("")
clock('listcomp         :', '[ord(s) for s in symbols]')
clock('for statement    :', FOR_STATEMENT)
print("")
print("")
print("")