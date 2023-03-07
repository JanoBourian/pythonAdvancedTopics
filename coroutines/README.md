# Coroutines

Exist a little difference between Generators and Coroutines. Generators can suspend the memory, but they can't receive information and can't catch exceptions while the process is running. 

## Three importants methods

```python
generator.send(value)
generator.throw(exception)
generator.close()
```

## Difference 

Exists a lot of difference beteween Coroutine and other kind of concepts:

- **Coroutine vs Routine or Subroutine.** Routine or subroutine is a function (part of a process)
- **Coroutine vs generator.** Coroutine is high level in comparsion to generator, Python used to use generators for cooperative multitasking. Generator can suspend and resume the executiong, but use the *yield* expression instead of the *await* expression.
- **Coroutine vs Task.** Task is a set of Coroutines to run in a for loop. 
- **Coroutine vs Thread.** Ok, Corourine is a special function, but Thread is an object that allows that the operative system manage the execution.
- **Coroutine vs Process.** Process is managed by the operative system and basicly is a program. 

## Important statments

```python
import asyncio
async def name_function():
    task1 = asyncio.create_task(
        other_function()
    )

    await tast1

asyncio.run(name_function())
```

Since Python 3.11 you can use the Context Manager for controlling the execution of tasks

```python
async def with_context():
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
```

```python
```

```python
```

```python
```