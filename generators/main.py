def fibo_sequence(max_number:int):
    a = 0
    b = 1
    total = 0
    while total < max_number:
        (yield a)
        total += 1
        a, b = b, a + b

fib = fibo_sequence(9)
for f in fib:
    print(f)

print("*"*100)

def counter(maximum:int):
    i = 0
    while i < maximum:
        val = (yield i)
        if val is not None:
            i = val
        else:
            i += 1

numbers = counter(15)
for i in numbers:
    if i*5 == 25:
        numbers.send(13)
    print(i)


print("*"*100)
input()
# numbers = counter(15)
# for i in numbers:
#     if i*5 == 25:
#         numbers.throw(ValueError)
#     print(i)


# print("*"*100)

numbers = counter(15)
for i in numbers:
    if i*5 == 25:
        numbers.close()
    print(i)


print("*"*100)