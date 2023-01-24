numbers = [1, 3, 5]

double = [x*2 for x in numbers ]
print(double)

v = [x for num in numbers if (x := num%2) != 0]
print(v)