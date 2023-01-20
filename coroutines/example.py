from random import randint
import time 
import asyncio 

def coro():
    step = 0
    while True:
        received = yield step
        step += 1
        print(f"RECEIVED: {received}")

def odds(start, stop):
    for odd in range(start, stop + 1, 2):
        yield odd

def main():
    odds1 = [odd for odd in odds(3, 15)]
    odds2 = tuple(odds(21, 29))
    print(odds1, odds2)

main()