from functools import wraps

def a_new_decorator(a_func):
    
    @wraps(a_func)
    def wrap_the_function():
        print("Decorator, before")
        a_func()
        print("Decorator, after")
        
    return wrap_the_function

@a_new_decorator
def a_function_with_decorator():
    print("Hello my friend")

a_function_with_decorator()