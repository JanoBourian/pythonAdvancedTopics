example_list = ["A", "B", "C"]

for counter, letter in enumerate(example_list):
    print(f"{counter} - {letter}")

people = [
    ("Bob", 42, "Mechanic"),
    ("James", 24, "Artist"), 
    ("Harry", 32, "Lecture")
]

for name, age, profesion in people:
    print(f"Name: {name}, Age: {age}, Profesion: {profesion}")

# Ignoring values
person = ("Bob", 42, "Mechanic")

name, _, profesion = person
print(name, profesion)

# Collect Values
numbers = [0,1,2,3,4,5,6,7,8,9]

start, *rest = numbers
print(start)
print(rest)

*start, rest = numbers
print(start)
print(rest)

start, *middle, tail = numbers
print(start)
print(middle)
print(rest)