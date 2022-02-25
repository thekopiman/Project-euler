#!/usr/bin/env python3
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def check_palindromic(number : int): # returns True or False
    list_number = list(str(number))
    list_number.reverse()
    if list_number == list(str(number)):
        return True
    else: return False

dictionary = {} # {product : (i,j)}
list_of_products = []
lst = list(range(100,1000))
lst.reverse()
for i in lst:
    for j in lst:
        if check_palindromic(i*j):
            # print(i,'*',j,'=',i*j)
            dictionary[i*j] = (i,j)
            list_of_products.append(i*j)
            break
print(dictionary[max(list_of_products)][0],'*',dictionary[max(list_of_products)][1],'=',max(list_of_products)) 
# 913 * 993 = 906609


