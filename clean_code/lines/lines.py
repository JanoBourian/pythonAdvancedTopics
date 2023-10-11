# Line length 79 characters
# Comments and docstring will be less of 72 characters
# In teams the maximum length is of 99 characters

game_board = [
    0, 0, 1, 0, 
    2, 0, 0, 1, 
    0, 0, 0, 1
    ]

pizza_order = {
    "size": "large", 
    "toppings": ["basil", "mushrooms", "olives"]
    }

def format_string(string:str) -> tuple:
    string.split("")
    return (string)

price = 50
tax = 5
discount = 1
coupons = 2
total_price = price \
            + tax \
            - discount \
            - coupons
            
total_price = (price 
               + tax 
               - discount 
               - coupons)