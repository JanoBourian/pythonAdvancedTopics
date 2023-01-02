import animal

class Bird(animal.Animal):
    
    def __init__(self, name):
        super().__init__(name)
    
piggote = Bird("Napoles")
print(piggote)
