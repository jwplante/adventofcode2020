# Advent of Code 2020 Day 7-1
# James Plante

import sys
import string
import re

class Edge:
    to = ""
    weight = 0
    
    # Constructor
    def __init__(self, to: str, weight: int):
        self.to = to
        self.weight = weight

    def __repr__(self):
        return "Edge(to: {}, weight: {})".format(self.to, self.weight)

INF = 99999

"""
Given a string specifying a node, it creates a tuple with the 
key and an array of edges.
"""
def node_from_string(in_str: str):
    two_parts = in_str.strip(string.punctuation).split("contain ")
    remove_bags = [re.sub(' *bag[s]* *','', s) for s in two_parts]
    
    key = remove_bags[0]
    neighbors = []
    if remove_bags[1] != 'no other':
        for deps in remove_bags[1].split(', '):
            all_words = deps.split()
            neighbors.append(Edge(' '.join(all_words[1:]), int(all_words[0])))
    return key, neighbors


"""
Converts a dictionary of vertices with adjacency list to a matrix
"""
def to_matrix_rep(graph: dict):
    vertices = len(graph)
    # Initialize
    matrix = [[INF for i in range(vertices)] for j in range(vertices)]
    # Doing a tuple swap since we want the keys to be the vertex
    vertex_dict = dict([(tup[1], tup[0]) for tup in enumerate(graph)])

    for vertex, edges in graph.items():
        for edge in edges:
            matrix[vertex_dict[vertex]][vertex_dict[edge.to]] = 1
    return matrix, vertex_dict

"""
Implementation of Floyd-Warshall to determine reachability of all bags to
every other bag
Reference: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
"""
def floyd_warshall(graph: dict):
    num_vertices = len(graph) 
    matrix, vertex_dict = to_matrix_rep(graph)
    
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return matrix, vertex_dict

"""
Main solution function
"""
def main_problem(input_string: str):
        graph = {}
        remove_empty_spaces = [line for line in input_string.split('\n') if line != '']
        # Generate the graph
        for line in remove_empty_spaces:
            key, value = node_from_string(line)
            graph[key] = value
        
        # Do Floyd-Warshall on the input
        final_matrix, vertex_dict = floyd_warshall(graph)

        # For each vertex, check if it can reach 'shiny gold', add
        # to counter
        counter = 0
        for vertex in final_matrix:
            if vertex[vertex_dict['shiny gold']] != INF:
               counter += 1
        print(counter)



if __name__ == "__main__":
    if (len(sys.argv) > 1):
        input_string = ""
        with open(sys.argv[1]) as f:
            input_string = f.read()
        
        main_problem(input_string)
        exit(0)
    else:
        print("Not enough arguments")

