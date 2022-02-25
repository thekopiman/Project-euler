#!/usr/bin/env python3
'''
The sum of the squares of the first ten natural numbers is,
1**2+2**2+...+10**2=385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)**2=55**2=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_of_squares(max_value):
    if max_value == 1:
        return 1
    
    elif max_value >= 1:
        return max_value**2 + sum_of_squares(max_value - 1)

def square_of_sum(max_value):
    x = 0
    for i in range(1, max_value + 1):
        x += i
    
    return x**2

print(square_of_sum(100) - sum_of_squares(100)) # 25164150
