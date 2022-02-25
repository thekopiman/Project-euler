#!/usr/bin/env python3
'''


The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.

'''


from math import *
from time import perf_counter

# def digit_power_sum(value):
#     sum_of_each_value = sum([int(x) for x in str(value)])
#     try:
#         power = log10(value)/log10(sum_of_each_value)
#         if round(power,3) == round(power):
#             # print(f"{power}: {value}")
#             if sum_of_each_value**round(power) == value:
#                 print(f"{round(power)}: {value}")
#                 return True
#     except ZeroDivisionError:
#         return False

def digit_power_sum(value):
    sum_of_each_value = sum([int(x) for x in str(value)])
    if sum_of_each_value != 1:
        factor = 1
        while sum_of_each_value**factor <= value:
            factor += 1
        if sum_of_each_value**(factor-1) == value:
            return True
        else: return False
    else: return False

sequence_values = []
current_count = 0
start = 10
start_time  = perf_counter()
while len(sequence_values) < 30:
    if digit_power_sum(start):
        sequence_values.append(start)
    # if current_count != len(sequence_values):
    #     print(current_count + 1)
    #     current_count = len(sequence_values)
    start += 1

# print(digit_power_sum(512))
print(sequence_values)
print(perf_counter() - start_time)

