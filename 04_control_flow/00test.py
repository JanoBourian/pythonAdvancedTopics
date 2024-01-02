# 4.1 if statements

def print_range(x_range:int) -> None:
    if x > 0:
        for i in range(x_range):
            print(f"{i}, ", end="")
    elif x == 0:
        print("Zero!")
    elif x < 0:
        print("Negative number")
    else: 
        print("Unexpected type value")
        

try:
    x = int(input("Ingresa un numero positivo: "))
    print_range(x)
except ValueError as ve:
    print(f"We found an error: {ve}")
except Exception as e:
    print(f"Error: {e}")