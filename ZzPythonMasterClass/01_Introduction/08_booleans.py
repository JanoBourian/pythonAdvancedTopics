# Booleans
yes = True
no = False
des = input("[yes/no]?: ")

if des == 'yes':
    print(yes)
else:
    print(no)

cast = {f"{i}": bool(i) for i in range(-2, 3)}
print(cast)

birth_year = input('what year were you born? ')

if type(2021 - int(birth_year)) == int:
    age = 2021 - int(birth_year)
    print(f"your age is: {age}")
else:
    print(f"your age is not a integer")
