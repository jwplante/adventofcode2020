# Advent of Code 2020 Day 3-1
# James Plante

import sys
import string

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        input_string = ""
        with open(sys.argv[1]) as f:
            input_string = f.read()
        
        # Parsing file into 2D array
        row = 0
        hill = []
        for line in input_string.split('\n'):
            if (line != ''):
                hill.append([])
                for char in line:
                    hill[row].append(char)
                row += 1
        
        counter = 0
        row = 0
        col = 0
        total_rows = len(hill) 
        total_cols = len(hill[0])

        while row < total_rows:
            if hill[row][col] == '#':
                counter += 1

            col = (col + 3) % total_cols
            row += 1

        print(counter)
        exit(0)
    else:
        print("Not enough arguments")

