picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for line in picture:
    for pix in line:
        if (pix):
            print('+', end="")
        else:
            print(' ', end='')
    print('')


def multiply(num):
    return num*2


def sum(num):
    return num+2


res = multiply(3)
print(res)

res = sum(3)
print(res)
