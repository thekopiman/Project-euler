#!/usr/bin/env python3
'''
Euler discovered the remarkable quadratic formula:

It turns out that the formula will produce 40 primes for the consecutive integer values . However, when is divisible by 41, and certainly when

is clearly divisible by 41.

The incredible formula
was discovered, which produces 80 primes for the consecutive values

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

, where and

where
is the modulus/absolute value of
e.g. and

Find the product of the coefficients,
and , for the quadratic expression that produces the maximum number of primes for consecutive values of , starting with .
'''

def quadratic(n, a, b):
    '''
    returns the output of f(n) = n**2 + a*n + b
    '''
    return n**2 + a*n + b

def check_prime(value : int):
    # Returns True if the value is prime else return False
    is_prime = True
    if value > 1:
        for i in range(2,value):
            if value%i == 0:
                is_prime = False
                break
        return is_prime
    else: return False    

if __name__ == "__main__":
    combinations = []
    for a in range(-999,1000):
        for b in range(-1000,1001):
            counter = 0
            is_consecutuve = True
            n = 0
            while is_consecutuve:
                if check_prime(quadratic(n, a, b)):
                    counter += 1
                    n += 1
                else: is_consecutuve = False
            combinations.append([counter, a , b])

    
    max_consecutive = max([x[0] for x in combinations])
    for x in combinations:
        if x[0] == max_consecutive:
            print(f"{x[1]}*{x[2]}={x[1]*x[2]}")
            break
    
    #-61*971=-59231