# Advent of Code 2020 Day 11-2
# James Plante
import sys
import string
import itertools
import copy


def total_seats(matrix: list):
  count = 0

  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == '#':
       count += 1 
  
  return count

def scan(i: int, j: int, coordinates: list):
  count = 0
  for i_offset in range(-1, 2):
    for j_offset in range(-1, 2):
      if not (i_offset == 0 and j_offset == 0):
        current_i = i + i_offset
        current_j = j + j_offset
        found = False
        while (not found and current_i >= 0 and current_j >= 0 and current_i < len(coordinates) and current_j < len(coordinates[0])):
          if coordinates[current_i][current_j] == '#':
            count += 1
            found = True
          elif coordinates[current_i][current_j] == 'L':
            found = True
          current_i += i_offset
          current_j += j_offset
  
  return count

"""
Main solution function
"""
def main_problem(input_string: str):
  lines = [i for i in input_string.split() if i != '']
  height = len(lines)
  width = len(lines[0])
  characters = [list(word) for word in lines]
  old = copy.deepcopy(characters)
  changed = True
  iteration = 0

  while changed:
    print('iteration: {}'.format(iteration))
    new = copy.deepcopy(old)
    for i in range(height):
      for j in range(width):
        surrounding = scan(i, j, old)
        if (surrounding == 0 and old[i][j] == 'L'):
          new[i][j] = '#'
        if (surrounding >= 5 and old[i][j] == '#'):
          new[i][j] = 'L'

    for elt in new:
      print(str(elt))

    changed = old != new
    iteration += 1
    old = new

    print(total_seats(old))
  


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
