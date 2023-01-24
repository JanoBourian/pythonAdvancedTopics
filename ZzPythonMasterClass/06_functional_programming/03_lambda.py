# lambda  param: action(param)

my_list = [1, 2, 3, 4]
print(list(map(lambda i: i**i, my_list)))


a = [(0, 2), (5, 2), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])

print(a)
