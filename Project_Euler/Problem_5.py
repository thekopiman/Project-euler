#!/usr/bin/env python3
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import Problem_3 


total_factors = []
for i in range(2,21):
    factors = Problem_3.prime_numbers(i)
    for j in factors:
        while factors.count(j) > total_factors.count(j):
            total_factors.append(j)

final_product = 1
for k in total_factors:
    final_product *= k

print(final_product) #232792560

