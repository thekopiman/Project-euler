#!/usr/bin/env python3
'''


Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

'''
import numpy as np

def clockwise_box(height, width = None):
    if width is None: width = height
    starting_coordinates = (height//2,height//2)
    zero_spiral = np.zeros([height,width],dtype=np.int32)
    current_coordinates = starting_coordinates
    current_direction = "RIGHT"
    previous_increment_value = 1
    increments = (1,0)
    for value in range(1, height*width +1):
        
        # print('Current Coordinates: ',current_coordinates)
        zero_spiral[current_coordinates[0],current_coordinates[1]] = value
        # print('Curent Spiral: \n',zero_spiral)
        # print('Current Direction: ',current_direction, "\n \n \n")
        
        
        if current_direction == "UP":
            current_coordinates = (current_coordinates[0] - 1,current_coordinates[1])
        elif current_direction == "DOWN":
            current_coordinates = (current_coordinates[0] + 1,current_coordinates[1])
        elif current_direction == "RIGHT":
            current_coordinates = (current_coordinates[0], current_coordinates[1] + 1)
        elif current_direction == "LEFT":
            current_coordinates = (current_coordinates[0],current_coordinates[1] - 1)
        
        
        increments = (increments[0] - 1, increments[1]) #The moment the increment is used, the increment[0] will minus 1
        '''
        If increments[0] reaches 0, the increments[1] will reset and the direction will change.
        '''
        if increments[0] == 0 and increments[1] == 0:
            current_direction = direction(current_direction)
            increments = (previous_increment_value, 1)
        
        elif increments[0] == 0 and increments[1] == 1:
            current_direction = direction(current_direction)
            previous_increment_value += 1
            increments = (previous_increment_value, 0)

    
    return zero_spiral


def direction(current_direction):
    if current_direction == 'UP':
        return 'RIGHT'
    elif current_direction == 'RIGHT':
        return 'DOWN'
    elif current_direction == 'DOWN':
        return 'LEFT'
    else: return 'UP'


def calculation(array):
    shape = array.shape
    total = 0
    for x in range(shape[0]):
        total += array[x,x]
    for x in range(shape[0]):
        total += array[x,shape[0]-x-1]
    return total - array[shape[0]//2, shape[1]//2]

if __name__ == "__main__":
    # print(clockwise_box(5,5))
    print(calculation(clockwise_box(1001,1001))) #669171001
