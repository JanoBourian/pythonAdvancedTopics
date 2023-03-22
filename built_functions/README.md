# Built functions

If you need more information please visit the official documentation in https://docs.python.org/3/library/functions.html

Basicly the Built-in functions are always available. Exist a lot of Built-in functions, here are all built-in functions with a brief description:

- **abs(x):**

Return the absolute value of int or float number. In case of complex number or some method that has implemented el method too.

<hr>

- **aiter(async_iterable)**

Return an async iterable. Euivalent to calling **x.\_\_aiter\_\_()**

<hr>

- **all(iterable)**

Return **True** if all elements of the iterable are true (or if the iterable is empty). Equivalent to:

```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

<hr>

- **anext(async_iterator)**
- **anext(async_iterator, default)**

Basicly is like **next()** operation but for awaitables iterators (or aiter())

<hr>

- **any(iterable)**

Return **True** if any element of the iterable is true. If the iterable is empty return **False**

```python
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```

<hr>

- **ascii(object)**

Return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned.

<hr>

- **bin(x)**

Converte an integre number to a binary stirng prefixed with "0b"

<hr>

- **bool(x=False)**

Return a Boolean value.

<hr>

- **breakpoint(*args, **kws)**

A powerfull way to debug o put breakpoints into a script or more complex python code.

```python
from dataclasses import dataclass

@dataclass
class Information:
    mesagge: str
    available_days: int

x = Information("Hello my friend", 15)
breakpoint()
x.mesagge
breakpoint()
x.available_days
```

Options: 
- c continue execution
- n step to the next line within the same function
- s step to the next line in this function or a called function
- q quit the debugger/execution

<hr>

- **bytearray(source = 'b')**
- **bytearray(source, encoding)**
- **bytearray(source, encoding, errors)**

Return a new array of bytes.

<hr>

- **bytes(source = 'b')**
- **bytes(source, encoding)**
- **bytes(source, encoding, errors)**

Return a new "bytes" object which is an inmutable sequence of integers.

<hr>

- **callable()**

Return True if the object is a callable (function, in other therms if the object can be executable)

```python
array = [1, 2, 3]
function = lambda x: x + 1
print(f"Function {callable(function)}")
print(f"Array: {callable(array)}")
```

<hr>

- **chr()**

Return the string representation to a value:

```python
for _ in range(0, 128):
    print(chr(_))
```

<hr>

- **classmethod()**

Method that can auto-instance. Check decorators for more information.

<hr>

- **compile(source, filename, mode, flags=0, dont_inherit = False, optimize = -1)**

```python
# Creating sample sourcecode to multiply two variables
# x and y.
srcCode = 'x = 10\ny = 20\nmul = x * y\nprint("mul =", mul)'
 
# Converting above source code to an executable
execCode = compile(srcCode, 'mulstring', 'exec')
 
# Running the executable code.
exec(execCode)
```

<hr>

- **complex(real = 0, imag = 0)**
- **complex(string)**

Return a complex number with the value __real + imag*j__

<hr>

- **delattr(object, name)**

Delete an atribuite. 


<hr>

- **class dict(\*\*kwargs)**
- **class dict(mapping, \*\*kwargs)**
- **class dict(iterable, \*\*kwargs)**

Create a new dictionary.

<hr>

- **dir()**
- **dir(object)**

Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.

```python
class PersonalClass:
    
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress
    
    def __dir__(self):
        return ["name"]

p = PersonalClass("james", 18, "St. Petesburgh")
print(dir(p))
print(p.age)
```

<hr>

- **divmod(a, b)**

For integers: a // b,  a % b


<hr>

- **enumerate(iterable, start = 0)**

Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.

```python
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
```

<hr>

- **eval(expression, globals = None, locals = None)**

The arguments are a string and optional globals and locals. If provided, globals must be a dictionary. If provided, locals can be any mapping object.

<hr>

- **exec(object, globals=None, locals=None, /, *, closure=None)**

Execute code directly.

<hr>

- **filter()**
<hr>

- **float()**
<hr>

- **format()**
<hr>

- **frozenset()**
<hr>

- **getattr()**
<hr>

- **globals()**
<hr>

- **hasattr()**
<hr>

- **hash()**
<hr>

- **help()**
<hr>

- **hex()**
<hr>

- **id()**
<hr>

- **input()**
<hr>

- **int()**
<hr>

- **isinstance()**
<hr>

- **issubclass()**
<hr>

- **iter()**
<hr>

- **len()**
<hr>

- **list()**
<hr>

- **locals()**
<hr>

- **map()**
<hr>

- **max()**
<hr>

- **memoryview()**
<hr>

- **min()**
<hr>

- **next()**
<hr>

- **object()**
<hr>

- **oct()**
<hr>

- **open()**
<hr>

- **ord()**
<hr>

- **pow()**
<hr>

- **print()**
<hr>

- **property()**
<hr>

- **range()**
<hr>

- **repr()**
<hr>

- **reversed()**
<hr>

- **round()**
<hr>

- **set()**
<hr>

- **setattr()**
<hr>

- **slice()**
<hr>

- **sorted()**
<hr>

- **staticmethod()**
<hr>

- **str()**
<hr>

- **sum()**
<hr>

- **super()**
<hr>

- **tuple()**
<hr>

- **type()**
<hr>

- **vars()**
<hr>

- **zip()**
<hr>

- **\_\_import\_\_()**
<hr>
