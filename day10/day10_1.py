# Advent of Code 2020 Day 10-1
# James Plante

import sys
import string
import itertools

"""
Main solution function
"""
def main_problem(input_string: str):
    all_numbers = [int(number) for number in [x for x in input_string.split('\n') if x != '']]
    all_numbers.sort()
    prev = 0
    adapter_frequencies = {}
    for i in all_numbers:
        if (i - prev not in adapter_frequencies):
            adapter_frequencies[i - prev] = 1
        else:
            adapter_frequencies[i - prev] += 1
        prev = i

    if (1 in adapter_frequencies and 3 in adapter_frequencies):
        adapter_frequencies[3] += 1
        print(adapter_frequencies[1] * adapter_frequencies[3])


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        PREAMBLE = int(sys.argv[2])
    if len(sys.argv) >= 2:
        input_string = ""
        with open(sys.argv[1]) as f:
            input_string = f.read()
        
        main_problem(input_string)
        exit(0)
    else:
        print("Not enough arguments")

