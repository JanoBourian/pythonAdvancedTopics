# Standard Library

Here is a brief tour trough the most important libraries (and functionalities, of course) in python.

## Operating System Interface

The os module provides dozens of functions for interacting with the operating system.

```python
import os
import shutil
help(os.path)
```

## File Wildcards

The glob module provides a function for making file lists from directory wildcard searches.

```python
import glob
print(glob.glob("*.py"))
```

## Command Line Arguments

Is for process command line arguments and to process line arguments (argparse, check documentation).

```python
import sys
print(sys.argv)
sys.exit()
import argparse
```

## Error Output Redirection and Program Termination

The sys module also has attributes for stdin, stdout, and stderr. The latter is useful for emitting warnings and error messages to make them visible even when stdout has been redirected

```python
sys.stdout.write('Warning, log file not found starting a new one\n')
```

## String Pattern Matching

The re module provides regular expression tools for advanced string processing. For complex matching and manipulation, regular expressions offer succinct, optimized solutions

```python
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
```

## Mathematics

```python
import math
print(dir(math))

import random
print(dir(random))

import statistics
print(dir(statistics))
```

## Internet Access

That is amazing because python provide you a two important libraries for internet access. 

```python
import urllib
import urllib.request
import smtplib

print(dir(urllib))
print(dir(urllib.request))
print(dir(smtplib))

from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())  
```

## Date and times

The datetime module supplies classes for manipulating dates and times in both simple and complex ways.

```python
from datetime import date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = date(1990, 9, 19)
age = now - birthday
print(age.days)
```

## Data Compression

Common data archiving and compression formats are directly supported by modules including: zlib, gzip, bz2, lzma, zipfile and tarfile.

```python
import zlib
s = b'witch which has which witches wrist watch'
len(s)
```

## Performance Measurement

```python
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
```

cProfile

```python
## Meassure time
def return_value(a:int) -> int:
    suma_result = 0
    for i in range(0, a):
        suma_result += i
    return suma_result

from timeit import Timer
import cProfile
cProfile.run("return_value(99999999)")

import time
start = time.perf_counter()
return_value(99999999)
print(f"TIME: {time.perf_counter() - start} ")
```

## Quality Control

One approach for developing high quality software is to write tests for each function as it is developed and to run those tests frequently during the development process.

The first way to take over quality is with **doctest**

```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
```

And the other way is with **unittest**

```python
import unittest

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```

## Batteries Included

The xmlrpc.client and xmlrpc.server modules make implementing remote procedure calls into an almost trivial task. Despite the modules’ names, no direct knowledge or handling of XML is needed.


The email package is a library for managing email messages, including MIME and other RFC 2822-based message documents. Unlike smtplib and poplib which actually send and receive messages, the email package has a complete toolset for building or decoding complex message structures (including attachments) and for implementing internet encoding and header protocols.


The json package provides robust support for parsing this popular data interchange format. The csv module supports direct reading and writing of files in Comma-Separated Value format, commonly supported by databases and spreadsheets. XML processing is supported by the xml.etree.ElementTree, xml.dom and xml.sax packages. Together, these modules and packages greatly simplify data interchange between Python applications and other tools.


The sqlite3 module is a wrapper for the SQLite database library, providing a persistent database that can be updated and accessed using slightly nonstandard SQL syntax.


Internationalization is supported by a number of modules including gettext, locale, and the codecs package.

## Output Formatting

The reprlib module provides a version of repr() customized for abbreviated displays of large or deeply nested containers:

```python
import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```

The pprint module offers more sophisticated control over printing both built-in and user defined objects in a way that is readable by the interpreter.

```python
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```

The textwrap module formats paragraphs of text to fit a given screen width:

```python
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```

The locale module accesses a database of culture specific data formats.

```python
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
locale.format("%d", x, grouping=True)
'1,234,567'
locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
```

## Templating

The string module includes a versatile Template class with a simplified syntax suitable for editing by end-users. This allows users to customize their applications without having to alter the application.

```python
from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```

The substitute() method raises a KeyError when a placeholder is not supplied in a dictionary or a keyword argument.

```python
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```

Template subclasses can specify a custom delimiter.

```python
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
```

## Workinh with Binary Data Record Layouts

The struct module provides pack() and unpack() functions for working with variable length binary record formats. 

```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```

## Multi-threading

```python
```

## Logging

For this part you can check the documentation in this repository or you can go to the oficial documentation: 

* https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
* https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial
* https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook

## Weak References

```python
```

## Tools for Working with lists

```python
```

## Decimal Floating Point Arithmetic

```python
```