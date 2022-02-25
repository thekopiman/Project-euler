#!/usr/bin/env python3
'''
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''
import time
number_of_ways = 0


for a in range(2):
    if a*200 == 200:
        print(f'{a}')
        number_of_ways += 1
        break
    for b in range(3):
        if a*200 + 100*b== 200:
            #print(f'{a} + 2*{b}')
            number_of_ways += 1
            break
        for c in range(5):
            if a*200 + 100*b + 50*c== 200:
                #print(f'{a} + 2*{b} + 5*{c}')
                number_of_ways += 1
                break
            for d in range(11):
                if a*200 + 100*b + 50*c + 20*d == 200:
                    #print(f'{a} + 2*{b} + 5*{c} + 10*{d}')
                    number_of_ways += 1
                    break
                for e in range(21):
                    if a*200 + 100*b + 50*c + 20*d + 10*e == 200:
                        #print(f'{a} + 2*{b} + 5*{c} + 10*{d} + 20*{e}')
                        number_of_ways += 1
                        break
                    for f in range(41):
                        if a*200 + 100*b + 50*c + 20*d + 10*e + 5*f == 200:
                            #print(f'{a} + 2*{b} + 5*{c} + 10*{d} + 20*{e} + 50*{f}')
                            number_of_ways += 1
                            break
                        for g in range(101):
                            if a*200 + 100*b + 50*c + 20*d + 10*e + 5*f + 2*g == 200:
                                #print(f'{a} + 2*{b} + 5*{c} + 10*{d} + 20*{e} + 50*{f} + 100*{g}')
                                number_of_ways += 1
                                break
                            for h in range(201):
                                if a*200 + 100*b + 50*c + 20*d + 10*e + 5*f + 2*g + h == 200:
                                    #print(f'{a} + 2*{b} + 5*{c} + 10*{d} + 20*{e} + 50*{f} + 100*{g} + 200*{h}')
                                    number_of_ways += 1
                                    break
                            
                                

print(number_of_ways)