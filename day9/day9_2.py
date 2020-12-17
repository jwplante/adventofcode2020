# Advent of Code 2020 Day 9-2
# James Plante

import sys
import string
import itertools

SUM = 15690279

"""
Computes wheter the subarray equals k in a brute-force way.
Will change if the running time is slow enough.
"""
def array_sum_equals_k(num_list: list, k: int):
    for length in range(2, len(num_list) + 1):
        for start in range(len(num_list) - length):
            total = sum(num_list[start: start + length])
            if total == SUM:
                print(min(num_list[start: start + length]) + max(num_list[start: start + length]))
                return


"""
Main solution function
"""
def main_problem(input_string: str):
    all_numbers = [int(number) for number in [x for x in input_string.split('\n') if x != '']]
    array_sum_equals_k(all_numbers, SUM)

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        SUM = int(sys.argv[2])
    if len(sys.argv) >= 2:
        input_string = ""
        with open(sys.argv[1]) as f:
            input_string = f.read()
        
        main_problem(input_string)
        exit(0)
    else:
        print("Not enough arguments")

