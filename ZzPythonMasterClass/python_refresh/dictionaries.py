friends_age = {"Rolf": 24, \
    "Anton": 31, \
        "Anne": 27}
for item in friends_age:
    print(friends_age[item])

for key, value in friends_age.items():
    print(f"{key} - {value}")

for item in friends_age.keys():
    print(item)

for item in friends_age.values():
    print(item)

# Comprehensions

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bs45dse."),
    (2, "Jose", "bdiueoi"),
    (3, "username", "buid0iojd"),
]

# user_mapping = {user[1]: user[2] for user in users if user[0]%2==0}
# print(user_mapping)

user_mapping = {user[1]: user for user in users}
print(user_mapping)

user_input = str(input("Enter your username: "))
user_password = str(input("Enter your password: "))

_, username, password = user_mapping[user_input]

if user_password == password:
    print(f"Welcome {username}")
else:
    print("Your details are incorrect!")