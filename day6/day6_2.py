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
            answers = {}
            parsed_input = group_answers.replace('\n', '')

            # Go through each group and get frequencies
            for char in parsed_input:
                if (char not in answers):
                    answers[char] = 1
                else:
                    answers[char] += 1

            groups = [x for x in group_answers.split('\n') if x != ""]

            # Add all of the instances where the dictionary
            for k, v in answers.items():
                if (v == len(groups)):
                    counter += 1
            
        print(counter)
        exit(0)
    else:
        print("Not enough arguments")

