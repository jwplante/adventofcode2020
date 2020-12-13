# Advent of Code 2020 Day 1-2
# James Plante

import sys
import string

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        input_string = ""
        with open(sys.argv[1]) as f:
           input_string = f.read()
        
        dictionary = {}

        for line in input_string.split("\n"):
            if line != "":
                int_value = int(line.strip(string.whitespace))
                dictionary[int_value] = int_value

        for key, value in dictionary.items():
            for inner_key, inner_value in dictionary.items():
                if (2020 - key - inner_key) in dictionary:
                    print(key * inner_key * (2020 - key - inner_key))
                    exit()

    else:
        print("Not enough arguments")

