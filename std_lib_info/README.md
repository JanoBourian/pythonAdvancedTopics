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

cProgfile

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

```python
```

## Templating

```python
```

## Workinh with Binary Data Record Layouts

```python
```

## Multi-threading

```python
```

## Logging


```python
```

## Weak References

```python
```

## Tools for Working with lists

```python
```

## Decimal Floating Point Arithmetic

```python
```