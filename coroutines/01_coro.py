import asyncio 
import time 

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World!")

asyncio.run(main())

async def new_message(first:str = "", second:str = "", time:int = 2):
    print(first)
    await asyncio.sleep(time)
    print(second)
    
asyncio.run(new_message("Primero del primero", "Segundo del primero", 1))
asyncio.run(new_message("Primero del segundo", "Segundo del segundo", 1))

## But with awaitable

async def test():
    print(f"Started at {time.strftime('%X')}")
    await new_message("Random", "Access", 1)
    await new_message("Memory", "Sigma", 1)
    print(f"Finished at {time.strftime('%X')}")

asyncio.run(test())

## But with tasks

async def with_tasks():
    task1 = asyncio.create_task(
        new_message("task1 started", "task1 finished", 5)
    )
    task2 = asyncio.create_task(
        new_message("task2 started", "task2 finished", 8)
    )
    print(f"Started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"Finished at {time.strftime('%X')}")

asyncio.run(with_tasks())

## But with the context manager

async def with_context():
    print("***** INSIDE with Context Manager ****")
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            new_message("Inside a first context", "Outside from first context", 10)
        )
        task2 = tg.create_task(
            new_message("Inside a second context", "Outside from second context", 12)
        )
        
        print(f"Started {time.strftime('%X')}")
        ## The await is implicit when the context manager exists.
        
    print(f"Finished {time.strftime('%X')}")

asyncio.run(with_context())