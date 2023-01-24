# Strings
word = "Hi, hello! I'm Francisco"
print(word)
print(type(word))
print(dir(str))

long_string = """
This is a message by @janobourian.
Good vibes
"""
print(long_string)

print(long_string, word)

# Type conversion
number = str(100)
print(number)
print(type(number))

print(int(number))
print(type(int(number)))

# Scape secuences
print("Hola \' \' \"  \" \' \n")
print("Hola \' \' \"  \" \'", end="\n\n")

# Formatted strings
name = 'Francisco'
last_name = 'González'
age = 30

print("Hi {0} {1}. Your age is: {2} ".format(name, last_name, age))
print("Hi {name} {last_name}. Your age is: {age} ".format(
    name='Fernando', last_name='Vallejo', age=30))
print(f"Hi {name} {last_name}. Your age is: {age}")

# Indexes

python = 'I am PYHTON'
# [start:stop:stepover]
print(python[1:4])
print(python[1:])
print(python[:])
print(python[1:100])
print(python[-1])
print(python[-4])
print(python[:-3])
print(python[-3:])
print(python[::-1])
