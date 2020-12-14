# Advent of Code 2020 Day 6-1
# James Plante

import sys
import string
import re

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        input_string = ""
        with open(sys.argv[1]) as f:
            input_string = f.read()

        counter = 0
        for group_answers in input_string.split('\n\n'):
            unique_answers = set()
            parsed_input = group_answers.replace('\n', '')
            for char in parsed_input:
                unique_answers.add(char)
            counter += len(unique_answers)
            
        print(counter)
        exit(0)
    else:
        print("Not enough arguments")

