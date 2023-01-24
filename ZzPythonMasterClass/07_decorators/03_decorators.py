# Decorator
def my_decorator(func):
    print("my_decorator")

    def wrap_func():
        print("wrap_func")
        func()
    return wrap_func


# @my_decorator
def hello():
    print('Hello!')


# hello()

a = my_decorator(hello)
a()
