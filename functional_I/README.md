# Functional I

Here we going to learn about the firsts (or basics) functions in functional programming. Maybe you have already seen these in other languages as Javascript. The concept is the same like other languages, but we need to review in a deepest way this topics.

## map
```python
map(function_to_apply, list_of_inputs)
```

## filter
```python
filter(function_to_apply, list_of_inputs)
```

## reduce
Take the two first position to start with the process, and after that continue with the next value using the last obteined

```python
import functools
result = functools.reduce(lambda x, y: x+y, list_of_values)
print(result)
```