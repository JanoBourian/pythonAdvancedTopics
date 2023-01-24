def divide(dividend, divisor):
    if divisor == 0: 
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend/divisor

grades = []

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e :
    print(f'Error: {e}')
else:
    print(f'average: {average:}')
finally: 
    print(f'Finally!')
