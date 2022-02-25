#!/usr/bin/env python3
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import math

multiples = []

def adding_multiples(value):
    global multiples
    multiple = 1
    while multiple*value < 1000:
        try:
            if multiples.index(multiple*value) != -1:
                multiples.append(multiple*value)
                multiple += 1
        except ValueError:
                multiples.append(multiple*value)
                multiple += 1

if __name__ == "__main__":
    adding_multiples(3)
    adding_multiples(5)
    # print(multiples)
    print(sum(set(multiples))) # 233168

            

            




