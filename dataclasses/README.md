# Dataclasses

## Relevant information about dataclasses

- Has a *\_\_init\_\_()* method and *\_\_repr\_\_()* method by default

## Arguments inside dataclasses decorator

Before all, all parameters inside the decorator represents a specific dunder method.

More information about dunder methods: https://levelup.gitconnected.com/python-dunder-methods-ea98ceabad15

```python
@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False,
           match_args=True, kw_only=False, slots=False, weakref_slot=False)
class C:
    ...
```
## Arguments for dataclas decorator

- init: 
- repr: 
- eq: To compare if two objects are equals
- order: Boolean compairson with the next methods: it, le, gt, ge. 
- unsafe_hash: \_\_hash\_\_()
- frozen: setattr, delattr
- match_args: match_args
- kw_only:
- slots: 
- weakref_slot:

## Arguments for fields