# Map

## Basic in-line way
list_of_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squared = list(map(lambda x: x**2, list_of_values))
print(squared)

## Useful caso based on current job
information = {"susan": 130.0, "artur": 6.58, "noah":7.8}
converted_information = list(map(lambda x : x*0.051, information.values()))
print(converted_information)

def convert_pesos(amount:float, current_value:float)->float:
    return amount*current_value
converted_information = {key: convert_pesos(value, 0.051) for (key, value) in information.items()}
print(converted_information)

# Filter
odd_values = list(filter(lambda x: x%2 ==0, list_of_values))
print(odd_values)

# Reduce
import functools
result = functools.reduce(lambda x, y: x+y, list_of_values)
print(result)