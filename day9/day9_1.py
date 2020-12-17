# Advent of Code 2020 Day 9-1
# James Plante

import sys
import string
import itertools

PREAMBLE = 25

def validate(num_list: list, current_position: int):
    if (current_position <= PREAMBLE):
        return True
    else:
        preamble = num_list[current_position - PREAMBLE: current_position]
        for combination in itertools.combinations(preamble, 2):
            if combination[0] + combination[1] == num_list[current_position]:
                return True
        return False

"""
Main solution function
"""
def main_problem(input_string: str):
    all_numbers = [int(number) for number in [x for x in input_string.split('\n') if x != '']]
    for i in range(len(all_numbers)):
        if not validate(all_numbers, i):
            print(all_numbers[i])
            return

    print("All are valid")

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

