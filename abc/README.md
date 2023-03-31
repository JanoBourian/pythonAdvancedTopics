# About ABC (abstract base classes)
This classes does not containt implementations

For more information check the code: https://github.com/python/cpython/blob/3.10/Lib/abc.py

## More about

Abstract classes are relationed with **@staticmethod**, **@classmethod** and **@property** methods, and their have a specific methods for those operations:

```python
@abc.abstractmethod
@abc.abstractclassmethod
@abc.abstractstaticmethod
@abc.abstractproperty
abc.get_cache_token()
abc.ipdate_abstractmethods(cls)
```

## Exist some basic classes

```python
class abc.ABC
class abc.ABCMeta
```