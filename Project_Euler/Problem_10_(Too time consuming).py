#!/usr/bin/env python3
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def obtain_prime(max_prime_number):
    prime_number_lists = []
    starting_value = 2
    while True:
        is_prime = True
        for i in prime_number_lists:
            if starting_value%i == 0:
                is_prime = False
                break
            
        if is_prime:
            print(f"A new prime numer {starting_value} is found!")
            prime_number_lists.append(starting_value)
        
        if starting_value >= max_prime_number:
            break

        starting_value += 1
    
    return prime_number_lists

if __name__ == "__main__":
    print(sum(obtain_prime(2_000_000)))