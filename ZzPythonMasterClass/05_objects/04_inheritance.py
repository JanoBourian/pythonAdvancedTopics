# Users: Wizard, Archers, Ogres,

class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")

    pass


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: {self.num_arrows}")
    pass


class Ogres(User):
    pass


wizard1 = Wizard('Merlín', 1000)
archer1 = Archer('Robin', 20)

wizard1.attack()
archer1.attack()
print(wizard1)
wizard1.sign_in()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))
