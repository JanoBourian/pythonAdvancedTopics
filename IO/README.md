# Input Output

## Important for you

- str() readable for humans
- repr() readable for the interpreter

## File IO

Is too much important to know about __with()__ statement, because exists several ways to work with files, but __with()__ is very secure in contrast with working only with __open()__ statement. 

### __open()__ statement

Bellow you could see an example:

```python
f = open("file.txt", "r", encoding="utf-8")
f.read()
f.readline()
f.write()
f.close()
```

We have two statements that are no common:

```python
s.tell()
s.seek()
```

### json structure

Serializing: Process to convert a string representation.

For line:
```python
import json 

# result = json.dumps()
# result = json.loads()
```

For files:
```python
import json 

# result = json.dump()
# result = json.load()
```