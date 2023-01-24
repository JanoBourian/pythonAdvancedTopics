# list, set or dictionary comprehension

my_list = [i for i in 'hello']
print(my_list)

other_list = [num**2 for num in range(100) if num % 2 != 0]
print(other_list)

"""
other_list = [num**2 for num in range(100) if True]
print(other_list)
"""

# Sets:

my_list = {i for i in 'hello'}
print(my_list)

other_list = {num**2 for num in range(100) if num % 2 != 0}
print(other_list)

# Dictionary

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items() if value %
           2 == 0}

other_dict = {num: num*2 for num in [1, 2, 3]}
print(other_dict)
# Dict Comprehension

cast = {input('role? '): input('actor? ') for i in range(2)}
print(cast)


# Exercise

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)
