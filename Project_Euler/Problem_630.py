#!/usr/local/env python3

class Coordinates():
    def __init__(self):
        s0 = 290797
        existing_sets = {}
        with open("Existing_value_sets.txt", "r").readlines as existing:
            for line in existing:
                existing_sets[int(line.split(" ")[0])] = int(line.split(" ")[1])

    def sn_next(self):
        pass
            