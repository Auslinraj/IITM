#import library math

import math
print(math.sqrt(9))
print(math.factorial(5))

#import library random

import random
print(random.random())

#Import library calendar

import calendar
print(calendar.calendar(2021))
print(calendar.month(2021,7))

#another way of importing calendar

from calendar import *
print(month(2021,10))
print(calendar(2021))

#Import only month from calendar

from calendar import month
print(month(2021,8))

#import library as variable

import calendar as c
print(c.calendar(2021))
print(c.month(2021,5))

#import part of library as variable

from calendar import month as m
print(m(2021,6))