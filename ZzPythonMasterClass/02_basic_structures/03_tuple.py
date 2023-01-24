# Tuple
# Inmutable
my_tuple = (1, 2, 3, 4, 5, 5, 5)
print(my_tuple[1])
print(my_tuple)
print(5 in my_tuple)

user = {
    (1, 2): 'name',
    'force': 5,
    True: 3.5
}
print(user[(1, 2)])
print((1, 2) in user)

# Methods

new_tuple = my_tuple[1:4]
print(new_tuple)

x, y, z, *other = my_tuple
print(x)
print(y)
print(z)
print(other)

print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))

# For example a ubication in uber eats app
