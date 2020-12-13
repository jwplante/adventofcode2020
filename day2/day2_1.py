# Advent of Code 2020 Day 2-1
# James Plante

import sys
import string
import re

"""
Returns the number of instances of key in the string
@param string - input string
@param key - char instance
"""
def instances_of(string: str, key: str):
    counter = 0
    for char in string:
        if (char == key):
            counter += 1
    return counter

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
                
                total_instances = instances_of(inp, char)

                if total_instances >= minimum and total_instances <= maximum:
                    counter += 1

        print(counter)
        exit(0)
    else:
        print("Not enough arguments")

