# Advent of Code 2020 Day 7-2
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
Get the total number of bags in the graph starting from node 'node'
"""
def get_total_bags(graph: dict, vertex: str):
    if len(graph[vertex]) == 0:
        return 0
    else:
        counter = 0
        for edge in graph[vertex]:
            counter += edge.weight + edge.weight * get_total_bags(graph, edge.to)
        return counter

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

        print(get_total_bags(graph, 'shiny gold'))



if __name__ == "__main__":
    if (len(sys.argv) > 1):
        input_string = ""
        with open(sys.argv[1]) as f:
            input_string = f.read()
        
        main_problem(input_string)
        exit(0)
    else:
        print("Not enough arguments")

