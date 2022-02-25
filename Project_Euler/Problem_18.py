#!/usr/bin/env python3
'''


By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

'''


class TriangleSummation():
    def __init__(self, triangle_dictionary):
        self.original_triangle = triangle_dictionary
        self.triangle_dictionary = triangle_dictionary
        self.current_line = len(triangle_dictionary) - 2 #The algorithm will start on the second last line by default

    def comparison(self, index : int):
        '''
        Returns a tuple of (Highest value, Direction) 
        Direction is either 0 or 1 where 0 = Left , 1 = Right
        '''
        # if type(self.triangle_dictionary[self.current_line+1]) == tuple:
        #     next_line_list = [int(x[0]) for x in self.triangle_dictionary[self.current_line+1]]
        #     print("Did this run?")
        # else:
        #     print("Did this run???")
        #     next_line_list = [int(x) for x in self.triangle_dictionary[self.current_line+1]]
        try:
            next_line_list = [int(x) for x in self.triangle_dictionary[self.current_line+1]]
        except TypeError:
            next_line_list = [int(x[0]) for x in self.triangle_dictionary[self.current_line+1]]
        # print(next_line_list)
        if next_line_list[index] > next_line_list[index + 1]:
            return (next_line_list[index], 0)
        elif next_line_list[index] < next_line_list[index + 1]:
            return (next_line_list[index + 1], 1)
        else:
            self.same_adjacent_value()
            return (next_line_list[index], 0)


    def same_adjacent_value(self):
        '''
        Creates a new route which has the same answer. The second route will be the Right (1) route
        '''
        print("Same value, miraculous")
    def previous_line(self):
        self.current_line = self.current_line - 1

    def wrapper(self):
        while self.current_line >=0:
            new_list = []
            current_line_list = self.triangle_dictionary[self.current_line]
            for index in range(len(current_line_list)):
                # print((self.comparison(index)[0],self.comparison(index)[1]))
                new_list.append((int(current_line_list[index]) + self.comparison(index)[0],self.comparison(index)[1]))

            self.triangle_dictionary[self.current_line] = new_list
            # print(self.triangle_dictionary)
            self.current_line -= 1
        
        
    def routefinder(self):
        direction = str(self.triangle_dictionary[0][0][1])
        current_index = self.triangle_dictionary[0][0][1]
        
        for i in self.triangle_dictionary:
            if i != 0 and i != len(self.triangle_dictionary) - 1:
                direction = direction + str(self.triangle_dictionary[i][current_index][1])
                current_index += self.triangle_dictionary[i][current_index][1]
        
        
        return str(direction)
    
    def math_line(self, original_tri_dict):
        route = self.routefinder()
        current_index = 0
        # print(route)
        for i in original_tri_dict:
            if i != len(original_tri_dict) -1:
                print(original_tri_dict[i][current_index], end =' + ')
            else:
                print(original_tri_dict[i][current_index], end =' = ')
            try:
                current_index += int(route[i])
            except IndexError:
                continue


            
    


if __name__ == "__main__":
    triangle = '''
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    '''.split("\n")[1:16]

    tri_dict = {} # Stores the data of {[line]:[corresponding values]}
    for i in range(len(triangle)):
        tri_dict[i] = triangle[i].split()
    original_tri_dict = {}
    for i in range(len(triangle)):
        original_tri_dict[i] = triangle[i].split()


    trial1 = TriangleSummation(tri_dict)
    trial1.wrapper()
    # print(trial1.triangle_dictionary)
    # for i in trial1.triangle_dictionary:
    #     print(trial1.triangle_dictionary[i])
    # print(trial1.routefinder())
    # print(original_tri_dict)
    trial1.math_line(original_tri_dict)
    print(trial1.triangle_dictionary[0][0][0])

    # 75 + 64 + 82 + 87 + 82 + 75 + 73 + 28 + 83 + 32 + 91 + 78 + 58 + 73 + 93 = 1074
    
    