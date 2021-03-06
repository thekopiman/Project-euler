#!/usr/bin/env python3
'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
import Problem_3

has_RecursionError = False

def triangle_number(nth_value : int):
    global has_RecursionError
    if not has_RecursionError:
        try:
            if nth_value == 1:
                return 1
            else: 
                return nth_value + triangle_number(nth_value - 1)
        
        except RecursionError:
            has_RecursionError = True
            total = 0
            for i in range(1, nth_value + 1):
                total += i
            
            return total
    else: 
        total = 0
        for i in range(1, nth_value + 1):
            total += i
            
        return total

def prime_numbers_dict(value):
    lst_of_prime = Problem_3.prime_numbers(value)
    dictionary = {}
    for i in lst_of_prime:
        try:
            if list(dictionary.keys()).index(i) != 0:
                continue
        except ValueError:
            dictionary[i] = lst_of_prime.count(i)

    return dictionary


def divisors(value, prime_calculations = False):
    if not prime_calculations:
        divisor_list = []
        for i in list(range(1, round(value/2) + 1)):
            if value%i == 0:
                divisor_list.append(i)

        return len(divisor_list)+1
    
    else:
        total = 1
        dict_cal = prime_numbers_dict(value)
        for key in dict_cal:
            total *= (dict_cal[key] + 1)
        
        return total



if __name__ == "__main__":
    total_divisors = 0
    i = 1
    while total_divisors <= 500:
        total_divisors = divisors(triangle_number(i), prime_calculations=True)
        i += 1
    
    print(f"The {i-1}th triangle that gives a triangle number of {triangle_number(i-1)} has {total_divisors} divisors")
    #The 12375th triangle that gives a triangle number of 76576500 has 576 divisors
    
    
    
    # print(Problem_3.prime_numbers(190512000))

    # print(divisors(190512000, prime_calculations=True))
