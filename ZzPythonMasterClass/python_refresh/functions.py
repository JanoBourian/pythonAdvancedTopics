def hello(positional_argument, keyword, default_value="") -> None:
    print(f"Hello {positional_argument} {keyword} {default_value}")

def factorial(number:int) -> int:
    if number > 1:
        return factorial(number - 1)*number
    else:
        return 1

if __name__ == "__main__":
    hello("Honey", keyword= "1999", default_value="default")
    value = factorial(10)
    print(f"Factorial {value}")
    # Lambda Functions
    result = (lambda x : x + 1)(5)
    print(f"result: {result}")
