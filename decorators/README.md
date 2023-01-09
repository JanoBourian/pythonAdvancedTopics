# Decorators

The first approach is based on three important decorators used in a OOP: classmethod, staticmethod and property.

## The first three:
- staticmethod

**@staticmethod** is a method that doesn't need to be instanced.

- classmethod

This is maybe the most complex concept. **@classmethod** works as a factory method, because it returns an instance.

- property

Property decorator has a similar function that **setter** and **getter** in __Java__

```python
instance_4 = ShowDecorators("Aiton Taurus", "5599887720")
print(instance_4.number)
```

- example:

```python
class ShowDecorators:
    
    def __init__(self, name = "", number = ""):
        self.name = name
        self.number = number
    
    @property
    def number(self):
        _number = "-".join([self._number[:3], self._number[3:6],self._number[6:]])
        return _number
    
    @number.setter
    def number(self, number):
        if len(number) != 10:
            raise ValueError("Invalid phone number.")
        self._number = number
    
    @classmethod
    def create_basic_phone(cls, number):
        _cellphone = cls("Basic Phone", number)
        print(f"A basic phone was created {_cellphone}")
        return _cellphone
    
    @staticmethod
    def get_emergency_number() -> str:
        return "911"
    
    def __repr__(self):
        return "<ShowDecorators> name: {}, number: {}".format(self.name, self.number)
```

```python
class Casa:

	def __init__(self, precio):
		self._precio = precio

	@property
	def precio(self):
		return self._precio
	
	@precio.setter
	def precio(self, precio_nuevo):
		if precio_nuevo > 0 and isinstance(precio_nuevo, float):
			self._precio = precio_nuevo
		else:
			print("Por favor ingrese un precio valido.")

	@precio.deleter
	def precio(self):
		del self._precio

```

## Generar overview from decorator concept

Basically a decorator is a way of pass function an other function. Below has an example:

```python
def hi(name="yasoob"):
    print("Now we are inside the hi() function")
    print(f"NAME BEFORE: {name}")
    
    def greet():
        return "We are inside the greet() function"
    
    def welcome():
        return "We are inside the welcome() function"
    
    print(f"NAME AFTER: {name}")
    
    if name == "yasoob":
        return greet
    else:
        return welcome
    
a = hi()
print(a)
print(a())
```

Blueprint 

```python
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run
```

Decorators with arguments

```python
from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # Open the logfile and append
            with open(logfile, 'a') as opened_file:
                # Now we log to the specified logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()
# Output: myfunc1 was called
# A file called out.log now exists, with the above string

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()
# Output: myfunc2 was called
# A file called func2.log now exists, with the above string
```

Decorator classes

```python
class logit(object):

    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        print(log_string)
        # Open the logfile and append
        with open(self._logfile, 'a') as opened_file:
            # Now we log to the specified logfile
            opened_file.write(log_string + '\n')
        # Now, send a notification
        self.notify()

        # return base func
        return self.func(*args)



    def notify(self):
        # logit only logs, no more
        pass
```