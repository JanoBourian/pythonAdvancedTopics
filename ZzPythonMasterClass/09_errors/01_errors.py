# Error Handling

while True:
    try:
        age = int(input('what is your age?: '))
        print(age)
    except ValueError:
        print("please enter a number")
    else:
        print("Thank You!")
        break


def sum_function(num1, num2):
    try:
        return num1 + num2
    except:
        print("Error!")


sum_function('1', 2)
