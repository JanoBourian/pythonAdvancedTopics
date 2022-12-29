# Errors

## Introduction

We have two basic errors: syntax errors and exceptions. 

## Important information 

- We can write one message for a lot of exceptions, for example: 
```python
try:
    do_something()
except (RuntimeError, TypeError, NameError) as e:
    pass 
```

- We can access to information inside the exception:
```python
try:
    raise Exception('spam', 'eggs')
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)
    x, y = e.args
```

- We can develop our own Exceptions (based on Exception using inheritance):
```python
class InvalidDocument(Exception):
    def __init__(self, **kwargs):
        self.value = kwargs.get("value", "")
```

- I can create a try-except-else-finally clause or statement
```python
try:
    pass
except Exception as e:
    pass
else:
    pass
finally:
    pass
```

- Sometimes we need to relatione some exceptions, check more in the documentation. 