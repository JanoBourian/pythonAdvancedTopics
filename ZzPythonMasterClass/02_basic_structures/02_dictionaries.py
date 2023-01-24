# Dictionary

comp = {input("name?: "): input("age?: ") for i in range(2)}
print(comp)

dictionary = {
    'courses': ['python', 'javascript', 'django'],
    'active': True,
    'name': 'Fernando',
    'age': 30
}
print(dictionary)

# Keys needs to be inmutable
over = {
    123: [1, 2, 3],
    True: 'hello'
}

print(over)

# Dictionary Methods
print(dictionary.get('jobs', 'No exists'))
user = dict(name='JohnJohn')
print(user)
print('age' in dictionary)
print('jobs' in dictionary)
print('age' in dictionary.keys())
print('Fernando' in dictionary.values())
print(dictionary.items())
dictionary2 = dictionary.copy()
print(dictionary.clear())
print(dictionary)
print(dictionary2)
print(dictionary2.pop('courses'))
print(dictionary2)

print(dictionary2.popitem())
print(dictionary2)

print(dictionary2.update({'age': 21}))
print(dictionary2)
