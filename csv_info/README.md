# CSV

CSV has a lot of configurations and methods, because we need to write, read and delete information. All about **csv** is based on **with open()** statement. 

## Module Contents

- **csv.reader(csvfile, dialect='excel', **fmtparams)**

Example:

```python
import csv

with open("eggs.csv", newline ="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=" ", quotechar = "|")
    for row in spamreader:
        print(", ".join(row))
```

<hr>

- **csv.writer(csvfile, dialect='excel', **fmtparams)**

Example:

```python
import csv

info_to_write = [
    ["Spam Spam Spam Spam Spam Baked Beans"],
    ["Spam Lovely Spam Wonderful Spam"]
]

with open("eggs.csv", "w", newline="") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter = " ", quotechar = "|", quoting = csv.QUOTE_MINIMAL)
    for item in info_to_write:
        spamwriter.writerow(item)
```

<hr>

- **csv.register_dialect(name[, dialect[, **fmtparams]])**

Associate dialect with name.

<hr>

- **csv.unregister_dialect(name)**

Delete the dialect associated with name from the dialect registry. An Error is raised if name is not a registered dialect name.

<hr>

- **csv.get_dialect(name)**

Return the dialect associated with name. An Error is raised if name is not a registered dialect name. This function returns an immutable Dialect.

<hr>


- **cvs.list_dialects()**

Return the names of all registered dialects.

```python
print(csv.list_dialects())
```

<hr>

- **cvs.field_size_limit(\[new_limit\])**

Returns the current maximum field size allowed by the parser. If new_limit is given, this becomes the new limit.

```python
print(csv.field_size_limit())
```

<hr>

## Classes for Dictionaries. 

- **class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwars)**

Create an object that operates like a regular reader but maps the information in each row to a dict whose keys are given by the optional fieldnames parameter.

```python
with open("names.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["first_name"], row["last_name"])
```

<hr>

- **class csv.DictWriter(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwars)**

Create an object which operates like a regular writer but maps dictionaries onto output rows.

```python
with open("names.csv", "w", newline="") as csvfile:
    fieldnames = ["first_name", "last_name"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({"first_name": "Baked", "last_name": "Beans"})
    writer.writerow({"first_name": "Lovely", "last_name": "Spam"})
    writer.writerow({"first_name": "Wonderful", "last_name": "Spam"})
```

<hr>


## Dialects and Formatting parameters


<hr>


## Reader objects


<hr>


## Writer Objects

- **csvwriter.writerow(row)**
- **csvwriter.writerows(rows)**
- **DictWriter.writeheader()**

<hr>

## Examples

The simplest way to read a CSV file is:

```python
import csv
with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

Reading a file with an alternate format:

```python
import csv
with open('passwd', newline='') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)
```

The corresponding simplest possible writeing example is:

```python
import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)
```

With encoding:

```python
import csv
with open('some.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

Registering a dialect:

```python
import csv
csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)
with open('passwd', newline='') as f:
    reader = csv.reader(f, 'unixpwd')
```

With exceptions:

```python
import csv, sys
filename = 'some.csv'
with open(filename, newline='') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
```

```python
import csv
for row in csv.reader(['one,two,three']):
    print(row)
```
