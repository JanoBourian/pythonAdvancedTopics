import time
import asyncio 
import random

## abs(x) or similar x.__abs__()

result = int.__abs__(-3)
print(f"Result abs(): {result}")

## __aiter__(async_iterable) and __anext__(async_iterator,[default,]) 

async def all_resources(resource:str):
    resources = {
        "resource1": 1234, 
        "resource2": 2345, 
        "resource3": 3456, 
        "resource4": 4567,
        "resource5": 5678}
    
    value = random.randint(0, 1)
    print(f"VALUE: {value}")
    await asyncio.sleep(value)
    return resources.get(resource)

class ResourceTaker: 
    
    def __init__(self, resources:str) -> None:
        self.resources = resources
    
    def __aiter__(self):
        self.iter_resources = iter(self.resources)
        return self
    
    async def __anext__(self):
        try:
            r = next(self.iter_resources)
        except StopIteration:
            raise StopAsyncIteration
        return await all_resources(r)

async def main():
    print(f"Start at {time.strftime('%X')}")
    async for r in ResourceTaker(["resource1", "resource2", "resource9"]):
        print(r)
    print(f"End at {time.strftime('%X')}")
    
    r2 = ResourceTaker(["resource1", "resource2", "resource9"]).__aiter__()
    print(type(r2))
    print(dir(r2))
    print(await anext(r2))
    print(await anext(r2))
    print(await anext(r2))

asyncio.run(main())

## all(iterable)

lista1 = [1, 2, 3, 5]
lista2 = [1, 2, 3, 4]
iterat = (x==y for x,y in zip(lista1, lista2, strict=True))
result = all(iterat)
print(f"Result iterat {result}")

## any(iterable)

iterat = [True, False, False]
print(f"First example {any(iterat)}")

iterat = [False, False]
print(f"Second example {any(iterat)}")

iterat = [False, False, True]
print(f"Third example {any(iterat)}")

iterat = []
print(f"Last example {any(iterat)}")

## ascii(object)

print(f"ascii('ññññ') {ascii('ñññ')}")