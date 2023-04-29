import statistics
from statistics import mean
from timeit import timeit
import asyncio
from typing import List 

# Single implementation
def calculate_mean(items:List) -> float:
    sum_total = 0
    total = len(items)
    for i in items:
        sum_total = sum_total + i
    return sum_total / total

if __name__ == '__main__':
    print(statistics.mean([1, 2, 3, 4, 4]))
    print(mean([1, 2, 3, 4, 4]))
    print(calculate_mean([1, 2, 3, 4, 4]))
    
    using_import = timeit(stmt = "statistics.mean([1, 2, 3, 4, 4])", setup = "import statistics")
    using_from = timeit(stmt = "mean([1, 2, 3, 4, 4])", setup = "from statistics import mean")
    single_implementation = timeit(stmt = "calculate_mean([1, 2, 3, 4, 4])", setup = "from __main__ import calculate_mean")

    print(f"using_import time: {using_import}")
    print(f"using_from time: {using_from}")
    print(f"single_implementation time: {single_implementation}")

