# Advent of Code 2020 Day 5-2
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
    
        all_seats = set()
        for line in input_string.split('\n'):
            if (len(line) > 0):
                all_seats.add(get_seat_id(line))

        min_id = min(all_seats)
        max_id = max(all_seats)
        all_matches = [x for x in range(min_id, max_id + 1) if x not in all_seats]
        
        print(all_matches[1])
        exit(0)
    else:
        print("Not enough arguments")

