import asyncio
import time 

## General example

async def sleepy(duration: float):
    print("Sleeping...")
    await asyncio.sleep(duration)
    return 37

async def foo():
    value = await sleepy(1.0)
    return value

def main():
    coro = foo()
    print(coro)
    result = asyncio.run(coro)
    print(result)

main()

## More deeply example

async def agen(x):
    for i in range(x):
        yield i

async def another():
    async for v in agen(9999):
        print(v)

start = time.perf_counter()
coro_2 = another()
asyncio.run(coro_2)
print(f"END {time.perf_counter() - start} seconds")
input("Press enter to continue...")


start = time.perf_counter()
def gen(x):
    for i in range(x):
        yield i

def nother():
    for v in gen(9999):
        print(v)

nother()
print(f"END {time.perf_counter() - start} seconds")