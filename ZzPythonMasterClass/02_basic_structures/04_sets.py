# SETS
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(dir(set))
my_set.add(100)
my_set.add(0)
print(my_set)

my_list = [0, 1, 2, 3, 4, 4, 5, 6, 7, 6, 7, 8, 10, 10, 2]
print(my_list)
my_new_list = set(my_list)
print(my_new_list)

# For example a mail list
print(10 in my_new_list)
print(len(my_new_list))

# Methods
new_set = my_new_list.copy()

"""
.difference()
.discard()
.difference_update()
.intersection()
.isdisjoint()
.issubset()
.issuperset()
.union()
"""
