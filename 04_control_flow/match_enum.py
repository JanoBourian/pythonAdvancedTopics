from enum import Enum 

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

color = Color(input("Enter your choice of 'red', 'green', or 'blue: "))
print(color)

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green|")
    case Color.BLUE:
        print("I'm feeling the blues :(")
    