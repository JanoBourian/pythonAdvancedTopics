import array 
long_numbers = [1, 2, 3, 4, -5, 6, -10, 11]
numbers = array.array('q', long_numbers)
print(numbers)
print(numbers.tolist())