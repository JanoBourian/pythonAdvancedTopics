import operator

# Comparation
result = operator.__lt__(5, 9)
print(f"RESULT __lt__: {result}")

# Logical operations
result = operator.not_([5])
print(f"RESULT not_: {result}")

result = operator.truth([])
print(f"RESULT truth: {result}")

# Mathematical and bitwise

result = operator.__abs__(-10)
print(f"RESULT __abs__: {result}")

result = operator.__add__(-10, 5)
print(f"RESULT __add__: {result}")

result = operator.__and__(2, 5)
print(f"RESULT __and__: {result}")

result = operator.__floordiv__(12, 5)
print(f"RESULT __floordiv__: {result}")

