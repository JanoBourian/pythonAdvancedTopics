# Coroutines

Exist a little difference between Generators and Coroutines. Generators can suspend the memory, but they can't receive information and can't catch exceptions while the process is running. 

## Three importants methods

```python
generator.send(value)
generator.throw(exception)
generator.close()
```

## Difference between Generator and Coroutines 

Only one commit 