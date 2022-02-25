#!/usr/bin/env python3
'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
def value_checker(value,power=5):
    if value == sum([int(x)**power for x in str(value)]):
        return True
    else: return False

total = -1 #Take into account that 1**5 is not a sum

for i in range(6*9**5 + 1):
    if value_checker(i):
        total += i

print(total) #443839
