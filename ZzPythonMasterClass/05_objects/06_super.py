# Users: Wizard, Archers, Ogres,

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

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
    def __init__(self, name, email, password, power):
        User.__init__(self, name, email, password)
        Attack.__init__(self, power)


class Archer(User, Attack):
    def __init__(self, name,  email, password, power):
        super().__init__(name, email, password)
        Attack.__init__(self, power)


class Ogres(User):
    pass


wizard1 = Wizard('Gandalf', 'wizard1@mail.com', '*********', 90)
print(wizard1.email)
wizard1.player_attack()
archer1 = Archer('Legolas', 'elfo@mail.com', '*******', 30)
print(archer1.email)
archer1.player_attack()

print(Wizard.mro())
