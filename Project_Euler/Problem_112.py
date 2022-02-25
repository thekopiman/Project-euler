#!/usr/bin/env python3
'''
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''

def bouncy(value):
    '''
    Returns True or False
    '''
    previous_value = int(str(value)[0])
    
    increment_checker = True
    decrement_checker = True

    for digit in str(value):
       if int(digit) >= previous_value:
           previous_value = int(digit)
       else: 
           increment_checker = False
           break
    for digit in str(value):
       if int(digit) <= previous_value:
           previous_value = int(digit)
       else: 
           decrement_checker = False
           break
    
    if not increment_checker and not decrement_checker:
        return True
    else: return False


    

if __name__ == "__main__":
    bouncy_count = 0
    total_count = 100 #Values below and inclusive of 100

    while bouncy_count/total_count != 0.99:
        total_count += 1
        if bouncy(total_count):
            bouncy_count += 1

    print(total_count) #1587000
