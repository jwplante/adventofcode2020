# Advent of Code 2020 Day 3-2
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
        
        total_rows = len(hill) 
        total_cols = len(hill[0])

        # Tuples in column, row format
        slope_configs = [
                (1, 1), 
                (3, 1), 
                (5, 1), 
                (7, 1), 
                (1, 2)
                ]
        
        # Go through all of the configs
        multiplied_total = 1
        for delta_col, delta_row in slope_configs:
            row = 0
            col = 0
            counter = 0

            while row < total_rows:
                if hill[row][col] == '#':
                    counter += 1
                col = (col + delta_col) % total_cols
                row += delta_row

            multiplied_total *= counter

        print(multiplied_total)
        exit(0)
    else:
        print("Not enough arguments")

