#!/usr/bin/env python3
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def prime_numbers(number):
    prime_numbers_list = []
    divided_value = 2
    while True:
        if number >= divided_value:
            if number%divided_value == 0:
                number = number/divided_value
                prime_numbers_list.append(divided_value)
                # print(divided_value)
            else: divided_value += 1
        else: break

    return prime_numbers_list

if __name__ == "__main__":
    print(max(prime_numbers(600851475143))) #6857   














