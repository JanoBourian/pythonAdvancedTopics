# Tasks

Tasks is an object useful to create sequence of coroutines, for example in a for loop. 

## Task Cancellation 

Is important that the coroutines uses *try/except* stament, because that help us to robust our code. 

## Task Groups 

Remember when you created a coroutine you can create a lot of task inside a coroutine for execute those tasks.

## Sleeping 

If you have an event loop with full duration, you can use the sleep for avoid blocking it. 

```python
import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 15.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())
```

## Runing Tasks concurrently

The key is **asyncio.gather** 

For more information please check the file *03_factorial.py*