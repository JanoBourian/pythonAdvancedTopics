import urllib.request
import asyncio
import time
import random
import functools

with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()

async def get_method(url:str, index:int) -> int:
    res = None
    with urllib.request.urlopen(url) as response:
        res = response.code
    value = random.randrange(10)
    await asyncio.sleep(value)
    # print(index, res, value)
    return value
    

async def main():
    start = time.perf_counter()
    print(f"Start {time.strftime('%X')}")
    urls = ['http://python.org/' for _ in range(100)]
    background_tasks = set()
    for index, item in enumerate(urls):
        task = asyncio.create_task(get_method(item, index))
        background_tasks.add(task)
        
    L = await asyncio.gather(*background_tasks)
    TOTAL = functools.reduce(lambda a, b: a + b, L)
    print(f"Finish {time.strftime('%X')}")
    print(f"Seconds {time.perf_counter() - start}")
    print(f"TOTAL {TOTAL}")

asyncio.run(main())