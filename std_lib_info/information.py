import sys

## os information
import os
import shutil

print(dir(os))
# print(dir(help))
# help(os.path)

print(dir(shutil))

## File wildcards
import glob
print(glob.glob("*.py"))

## Command line arguments
import sys
print(sys.argv)

## Internet access

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
            
## Dates and times

from datetime import date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = date(1990, 9, 19)
age = now - birthday
print(age.days)

## Compression

import zlib
s = b'witch which has which witches wrist watch'
print(len(s))

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

## Doctest

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    
    >>> print(average([20, 30, 70]))
    60.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests