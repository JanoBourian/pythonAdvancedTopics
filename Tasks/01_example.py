import asyncio 
import time

async def async_count(sleep_time:int):
    # print(f"Time {sleep_time} seconds")
    print(f"Task {sleep_time}")
    await asyncio.sleep(sleep_time)
    return sleep_time
    # print(f"Time {sleep_time} seconds")

async def main():
    print(f"Start {time.strftime('%X')}")
    background_tasks = set()
    
    for i in range(10):
        task = asyncio.create_task(async_count(i))
        background_tasks.add(task)
        # task.add_done_callback(background_tasks.discard)
        
    for t in background_tasks:
        await t
        
    print(f"Finish {time.strftime('%X')}")
    
asyncio.run(main())