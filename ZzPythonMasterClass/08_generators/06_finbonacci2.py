def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        aux = a + b
        a = b
        b = aux


for i in fib(100):
    print(i, end=", ")

print("")
