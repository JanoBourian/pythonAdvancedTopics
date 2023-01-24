# Users: Wizard, Archers, Ogres,

class User:
    def __init__(self, name):
        self.name = name

    def sign_in(self):
        print('logged in')


class Attack:
    def __init__(self, power):
        self.power = power

    def player_attack(self):
        if (isinstance(self, Wizard)):
            print(f"attacking with power of {self.power}")
        elif (isinstance(self, Archer)):
            print(f"attacking with arrows: {self.power}")


class Wizard(User, Attack):
    def __init__(self, name, power):
        User.__init__(self, name)
        Attack.__init__(self, power)


class Archer(User, Attack):
    def __init__(self, name, power):
        User.__init__(self, name)
        Attack.__init__(self, power)


class Ogres(User):
    pass


wizard1 = Wizard('Gandalf', 90)
wizard1.player_attack()
archer1 = Archer('Legolas', 20)
archer1.player_attack()
