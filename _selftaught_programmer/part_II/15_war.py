import random 

# Card

class Card:
    
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    def __init__(self):
        """ suit + values are ints """
        self.value = random.choice(self.values) # v
        self.suit = random.choice(self.suits) # s
    
    def __repr__(self):
        return f"{self.value} - {self.suit}"

# Deck

# Player

# Game

## Testing
for _ in range(10):
    print(Card())

## All it together
