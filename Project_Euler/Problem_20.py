#!/usr/env/bin python3
'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def factorial(value):
    if value < 0:
        print("Must be a natural number")
        quit()
    if value == 1 or value == 0:
        return 1
    else:
        return value*factorial(value - 1)

print(sum([int(x) for x in list(str(factorial(100)))])) # 648