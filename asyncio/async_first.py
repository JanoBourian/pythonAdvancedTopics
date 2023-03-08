import asyncio 
import time

async def async_count(sleep_time:int):
    print(f"Time {sleep_time} seconds")
    await asyncio.sleep(sleep_time)
    print(f"Time {sleep_time} seconds")
    
async def main():
    async with asyncio.TaskGroup() as tasks:
        print(f"Start at {time.strftime('%X')}")
        task1 = tasks.create_task(async_count(1))
        task2 = tasks.create_task(async_count(2))
        task3 = tasks.create_task(async_count(3))
    print(f"Finish at {time.strftime('%X')}")
    print("Finished...")

asyncio.run(main())