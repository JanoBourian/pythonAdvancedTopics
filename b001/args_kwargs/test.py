# * is the unpacked iterator
nums = [1, 2, 3, 4, 5]
print(nums)
print(*nums)

# order_pizza(size, *toppings, **details)
def order_pizza(size:str, *args, **kwargs) -> None:
    print(f"I ordered a {size} pizza with the following toppings: {args} and the details: {kwargs}")

order_pizza("large", "extra cheese", "mushrooms", delivery = True, tax = 5)