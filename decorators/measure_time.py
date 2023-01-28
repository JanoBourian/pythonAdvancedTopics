import logging
from time import perf_counter
from collections.abc import Callable
from typing import Any
from typing import Generator

def prime_sequence(number:int) -> Generator:
    value = 2
    while value < number:    
        yield value
        value += 1

def is_prime(number:int) -> bool:
    gen = prime_sequence(number)
    while True:
        try:
            value = number % next(gen)
            if(value == 0):
                return False
        except StopIteration:
            break
    return True

def mesaure_time(func:Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args:Any, **kwargs:Any) -> Any:
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.warning(f"Exectuion of {func.__name__} took {run_time:.2f} seconds.")
        return result
    return wrapper

@mesaure_time
def count_prime_numbers(upper_bound:int) -> int:
    count = 0
    list_values = []
    for number in range(2, upper_bound):
        if is_prime(number):
            list_values.append(number)
            count += 1
    logging.warning(f"Prime values: {list_values}")
    return count

def main():
    print("Hello!")
    value = count_prime_numbers(100000)
    logging.warning(f"Prime numbers {value}")

if __name__ == '__main__':
    main()