#!/usr/bin/env python3
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''



def obtain_prime(number_of_primes):
    prime_number_lists = []
    starting_value = 2
    while len(prime_number_lists) < number_of_primes:
        is_prime = True
        for i in prime_number_lists:
            if starting_value%i == 0:
                is_prime = False
            
        if is_prime:
            prime_number_lists.append(starting_value)

        starting_value += 1
    
    return prime_number_lists

print(obtain_prime(10001)[-1]) #104743


