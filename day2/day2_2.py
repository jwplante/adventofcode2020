# Advent of Code 2020 Day 2-2
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
        for line in input_string.split('\n'):
            parsed_line = re.split("[-: ]", line)
            if (len(parsed_line) > 1):
                minimum = int(parsed_line[0])
                maximum = int(parsed_line[1])
                char = parsed_line[2]
                inp = parsed_line[4]

                if minimum - 1 < len(inp) and maximum - 1 < len(inp):
                    first_check = inp[minimum - 1] == char
                    second_check = inp[maximum - 1] == char
                    if (first_check and not second_check) or (not first_check and second_check):
                        counter += 1

        print(counter)
        exit(0)
    else:
        print("Not enough arguments")

