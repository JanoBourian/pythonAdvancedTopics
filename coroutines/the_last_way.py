import asyncio
import time 

## Coroutines

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("world")

asyncio.run(main())

# Simple coroutine

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main_2():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main_2())

# With Tasks

async def main_3():
    task1 = asyncio.create_task(
        say_after(5, "hello")
    )
    
    task2 = asyncio.create_task(
        say_after(7, "world")
    )
    
    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main_3())