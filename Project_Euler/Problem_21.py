#!/usr/bin/env python3
'''

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def sum_of_divisors(value):
    divisor_list = []
    for i in list(range(1, round(value/2) + 1)):
        if value%i == 0:
            divisor_list.append(i)
    return sum(divisor_list)

def amicable_numbers(value):
    '''
    Return True or False if the conditions below are followed
    d(a) = b
    d(b) = a
    '''

    a = value
    b = sum_of_divisors(value)

    if sum_of_divisors(b) == a:
        return True
    
    else: return False

if __name__ == "__main__":
    total = 0
    for number in range(1,10_000):
        if amicable_numbers(number):
            total += number

    print(total) # 40284