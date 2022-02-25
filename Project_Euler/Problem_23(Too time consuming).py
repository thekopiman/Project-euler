#!/usr/bin/env python3
'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import time 
from Problem_21 import sum_of_divisors

lst_of_abundant = []
start = time.perf_counter()
for value in range(28123):
    if value < sum_of_divisors(value):
        
        lst_of_abundant.append(value)
        
print(time.perf_counter() - start)

def non_abundant_sums(value):
    global lst_of_abundant
    is_abundant_sum = False
    for first in lst_of_abundant:
        for second in lst_of_abundant:
            if value == first+second:
                is_abundant_sum = True
                break
        if is_abundant_sum:
            break
    if not is_abundant_sum:
        return value
    else: return None
total = 0
for number in range(1,28123 + 1):
    if non_abundant_sums(number) == None:
        continue
    else: total += number

print(total)