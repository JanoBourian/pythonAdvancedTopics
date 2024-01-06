import random 

# Card

class Card:
    
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    def __init__(self):
        """ suit + values are ints """
        self.value = random.choice(self.values) # v
        self.suit = random.choice(self.suits) # s
    
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        return f"{self.value} - {self.suit}"

# Deck

# Player

# Game

## Testing
print("__lt__ comparison")
for _ in range(10):
    card_1 = Card()
    card_2 = Card()
    print(f"{card_1} < {card_2}: {card_1 < card_2}")

print("__gt__ comparison")
for _ in range(10):
    card_1 = Card()
    card_2 = Card()
    print(f"{card_1} > {card_2}: {card_1 > card_2}")

## All it together
