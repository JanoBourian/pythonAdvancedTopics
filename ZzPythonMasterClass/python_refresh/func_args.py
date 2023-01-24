def multiply(*args):
    total = 1
    print(f'args: {args}')
    for arg in args: 
        total = total * arg
        print(f'total: {total}')
    return total

print(multiply(1,2,3,4,5,6))

###
def add(x,y):
    print(x+y)

nums = [3,5]
add(*nums)

### 

nums2= {"x": 6, "y": 8}
add(**nums2)

###
# def apply(*args, operation):
#     if operation == '+':
#         return sum(args)
#     elif operation == '*':
#         print(f'args: {args}')
#         return multiply(args)
#     else: 
#         return "This is not a validate operation"

# result = apply(1,2,3,4,5,6,7, operation='*')
# print(f'result: {result}')