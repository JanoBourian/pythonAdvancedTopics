# Foor Loops
# iterable - list, dictionary, tuple, set, string
# iterated -> one by one check each item in the collection

for i in range(10):
    print(i, end=', ')
print(' ')

for item in 'Zero to mastery':
    print(item)

user = {
    'name': 'Francisco González Antonio',
    'age': 30,
    'is_programmer': True,
    'languages': ['python', 'javascript', 'c', 'c++', 'sql']
}

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for item in user.items():
    # print(item)
    key, value = item
    print(key, value)

for i in range(0, 10, 2):
    print(i)

lista = list(range(100))
print(lista)

# Enumerate
for char in enumerate('Helloooo'):
    print(char)

for item, char in enumerate('mexico'):
    print(f"{item} - {char}")

# While loops
count = 0
while count < 10:
    print(count)
    count += 1
else:
    print('done!.')

# break, continue, pass
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

"""
for i in range(len(picture)):
    for j in range(len(picture[i])):
        if picture[i][j] == 0:
            print('  ', end='')
        else:
            print('*', end=' ')
    print('')
"""
fill = '*'
empty = ' '

for line in picture:
    for pixel in line:
        if pixel == 0:
            print(empty, end='')
        else:
            print(fill, end='')
    print('')

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicate = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicate:
            duplicate.append(value)

print(some_list)
print(duplicate)
