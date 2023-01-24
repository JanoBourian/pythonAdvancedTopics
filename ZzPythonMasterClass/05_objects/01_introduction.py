"""
Remember my friend: all in python is an object
"""


class Drone():
    pass


simulink = Drone()

print(type(Drone))
print(type(simulink))


# OOP

class PlayerCharacter:
    membership = True

    def __init__(self, name='User'):
        self.name = name  # attributes

    def run(self) -> None:
        print(f'{self.name} run...')

    def __str__(self) -> str:
        return f"{self.name}"


player1 = PlayerCharacter('Alexander')
player2 = PlayerCharacter()

print(type(player1))
player1.run()
print(player1.name)
print(player2)
print(player2.name)
print(player2.membership)
player2.membership = False
print(player2.membership)


class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


ronald = Cat('ronald', 3)
dubster = Cat('dubster', 2)
sveltie = Cat('sveltie', 4)


def get_oldest_cat(*args):
    return max(args)


print(
    f"The oldest cat is {get_oldest_cat(ronald.age, dubster.age, sveltie.age)} years old.")
