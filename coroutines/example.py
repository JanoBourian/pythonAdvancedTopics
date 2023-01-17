def coro():
    step = 0
    while True:
        received = yield step
        step += 1
        print(f"RECEIVED: {received}")

