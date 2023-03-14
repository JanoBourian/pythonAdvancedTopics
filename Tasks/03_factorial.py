import asyncio
import time 

async def factorial(name:str, number:int) ->int:
    f = 1
    for i in range(2, number + 1):
        print(f"Time {time.strftime('%X')} - Task {name}: Compute factorial({number}), currently i={i}")
        await asyncio.sleep(1)
        f *= i
    print(f"Time {time.strftime('%X')} - Task {name}: factorial({number})={f}")
    return f
    

async def main():
    L = await asyncio.gather(
        factorial("A", 5),
        factorial("B", 10),
        factorial("C", 12),
    )
    print(L)
    print(type(L))

asyncio.run(main())