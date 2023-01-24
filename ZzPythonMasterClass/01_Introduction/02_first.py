print("Hello world!")
name = input('What is your name?: ')
print(F"Hi {name}!")
print("Hi " + name + "!")

# Some new features in Python 3.8

if (n := len(name)) > 10:
    # In this case, n = len(a)
    print(f"Have a {n} elements")

# Dict Comprehension

cast = {input('role? '): input('actor? ') for i in range(2)}
print(cast)

# Positional Arguments


def names(a, /, b, *, c):
    print(f"a = {a}, b = {b}, c = {c}")


names('Abel', 'Gerardo', c='Gabriel')
names('Abel', b='Gerardo', c='Gabriel')
# names('Abel', 'Gerardo', b='Gabriel', c='Francisco')
