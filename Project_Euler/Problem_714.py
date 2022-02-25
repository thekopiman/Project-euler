#!/usr/bin/env python3
'''
We call a natural number a duodigit if its decimal representation uses no more than two different digits. For example, , and are duodigits, while is not.
It can be shown that every natural number has duodigit multiples. Let be the smallest (positive) multiple of the number that happens to be a duodigit. For example, , , , and

.

Let
. You are given , and

.

Find
. Give your answer in scientific notation rounded to 13 significant digits (12 after the decimal point). If, for example, we had asked for instead, the answer format would have been 2.957098800000e7.
'''
def duodigits(value):
    '''
    Returns true or false
    '''
    if len(set(str(value))) <= 2:
        return True
    else: return False

def duodigits_multiple(value):
    x = value
    while not duodigits(x):
        x += value
    
    return x

def summation_duo(max_value):
    total = 0
    for i in range(1,max_value + 1):
        total += duodigits_multiple(i)
    return total
if __name__ == "__main__":
    print(summation_duo(50000))
        
    
    
