# asyncio

## Information

If you need a brief introduction to this topics maybe you can start with this video: https://www.youtube.com/watch?v=7AoANOGIDuM

In a general way you can check this: https://www.youtube.com/watch?v=GSiZkP7cI80

If you have more knowledge maybe you could see it: https://www.youtube.com/watch?v=6RbJYN7SoRs&t=11s

## Beatty example

```python
async def fetch(url:str) -> str:
    async with request("GET", url) as r:
        return await r.text("utf-8")

async def main():
    coros = [fetch(url) for url in URLS]
    results = await asyncio.gather(*coros)
    for result in results:
        print(f"{result[:20]!r}")
```