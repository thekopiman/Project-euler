#!/usr/bin/env python3
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
from math import ceil

for b in range(2,1000):
    c = (b**2 + (b-1000)**2)/(2000 - 2*b)
    if ceil(c) == c and c + b <= 998:
        print(f'c({b}) = {c}')

# c = 425, b = 200 or b = 375

for b in [200, 375]:
    a = 1000 - 425 - b
    if a**2 + b**2 == 425**2:
        print('a = ',a)

# a = 200, b = 375, c = 425