#!/usr/bin/env python3
'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def even(value):
    return value/2
def odd(value):
    return 3*value + 1


def starting(k):
    counter = 1
    n = k
    # print(n, end= '->')
    while not n <= 1:
        counter += 1
        if n%2 == 0:
            n = even(n)
            # print(n, end= '->')
        else:
            n = odd(n)
            # print(n, end= '->')
    
    if n <= 1:
        # print("\n")
        # print(f"There are {counter} terms for starting number {k}.")
        return counter

if __name__ == "__main__":
    longest_chain = (1,1) # (starting number, number of terms)
    for i in range(1, 1_000_000 + 1):
        if starting(i) >= longest_chain[1]:
            longest_chain = (i, starting(i))
    print(f"The longest chain is {longest_chain[0]} with {longest_chain[1]} terms.")
    
    #The longest chain is 837799 with 525 terms.


