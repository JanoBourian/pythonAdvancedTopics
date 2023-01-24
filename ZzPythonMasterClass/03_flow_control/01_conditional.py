is_old = True
is_licenced = True

if is_old is not True:
    print("Jojo!")
else:
    print("Darko!")

if False or True:
    print(f"is {False} or {True}")
elif True:
    pass
else:
    pass


# Truthy and Falsy
print(bool(''))
print(bool(0))
print(bool(5))
print(bool('Jojo!'))

username = 'username'
password = '123'

if username and password:
    print(f"{username} : {password}")
else:
    print("Not Available")

# Ternary Operator
is_friend = True
can_message = 'message allowed' if is_friend else "not allowed to message"
print(can_message)

# Short Circuiting
# and
# or
# not

# Logical operator
# <
# >
# >=
# <=
# ==
# !=

print(True == 1)  # True
print([] == [])  # True
print([] is [])  # False (different memory location)
