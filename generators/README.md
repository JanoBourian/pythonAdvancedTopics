# Generators

Generators are a beauty way to manage an iterable information or a long information. Generators are a special subset of Coroutines.

## main.py

This file has information about the correct way to work with a generator. Remember, the basis was iterator operations with the dunder methods: *iter* and *next*

## Important

- When you need pass information into a generator you can use three differents statments:
    - send(): With this method you put the new value inside of the *yield* statement.
    - throw(): You can throw exceptions inside a generator
    - close(): Close the generator