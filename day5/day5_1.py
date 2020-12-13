# Advent of Code 2020 Day 5-1
# James Plante

import sys
import string
import re

"""
Gets the Seat ID of the passenger given a BSP Ordering
"""
def get_seat_id(bsp_string: str):
    bitstring = re.sub("[BR]", '1', re.sub("[FL]", '0', bsp_string))
    row = int(bitstring[:7], 2)
    col = int(bitstring[7:], 2)
    return (8 * row) + col

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        input_string = ""
        with open(sys.argv[1]) as f:
            input_string = f.read()
        
        current_max = 0
        for line in input_string.split('\n'):
            if (len(line) > 0):
                current_max = max(current_max, get_seat_id(line))
        print(current_max)
        exit(0)
    else:
        print("Not enough arguments")

