# Lists
li = [1, 2, 3, 4]
li2 = ['a', 'b', 'c', 'd', 'e']
li3 = [1, 2.5, 3, 'a', True, False]

amazon_cart = [
    'notebooks',
    'sunglasses',
    'books',
    'toys',
    'grapes',
]

# List Slicing

amazon_cart.append('laptop')

for i in range(len(amazon_cart)):
    print(amazon_cart[i:len(amazon_cart)])

# Modify the list
new_cart = amazon_cart[:]
new_cart[0] = 'gum'

print(new_cart)
print(amazon_cart)

# Matrix

n = int(input("n?: "))
m = int(input("m?: "))


def matrix_definition(n, m) -> list:
    """ Return a Matrix of nxm
    n = int
    m = int
    """
    matrix = []
    for i in range(n):
        aux = []
        for j in range(m):
            data = input(f"[{i+1}][{j+1}]: ")
            aux.append(data)
        matrix.append(aux)
    return matrix


matrix = matrix_definition(n, m)

print(matrix)


def matrix_print(matrix) -> None:
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(f"{matrix[i][j]}", end=' ')
        print("")


matrix_print(matrix)

# List methods

# Adding methods
# matrix.append(value)
# matrix.insert(index, value)
# matrix.extends([])

# Removing methods
# matrix.pop() // matrix.pop(index)
# matrix.remove(value)
# matrix.clear()

# Others methods
# matrix.index(value, start, end)
# 'value' in matrix
# matrix.count(value)
# matrix.sort() // sorted(matrix) -> new copy
# matrix.reverse()

print('2' in matrix[1])  # True

print(list(range(100)))

# join and split
sentence = ' '
new_sentence = sentence.join(['Hi!', 'my', 'name', 'is', 'JOJO'])
print(new_sentence)
other_sentence = new_sentence.split(' ')
print(other_sentence)

# List unpacking

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers)
print(a)
print(b)
print(c)
print(other)
print(d)
