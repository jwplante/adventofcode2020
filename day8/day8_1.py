# Advent of Code 2020 Day 8-1
# James Plante

import sys
import string
import re


class Instruction:
    # Constructor
    def __init__(self, attr, value):
        self.attr = attr
        self.value = value

    def __repr__(self):
        return 'Instruction( {}, {} )'.format(self.attr, self.value)


class HandheldState:
    # Constructor
    def __init__(self):
        self.instructions = []
        self.instructions_used = []
        self.pc = 0
        self.acc = 0
    
    def __repr__(self):
        return 'Current State:\nPC:{} acc:{} instructions_used:{}'.format(self.pc, self.acc, self.instructions_used)

    """
    Factory method to create a new handheld state
    """
    def create_instance(instructions: str):
        new_handheld = HandheldState()
        in_list = [line for line in instructions.split('\n') if line != '']
        for instruction in in_list:
            attr = instruction.split()[0]
            value = int(instruction.split()[1])
            to_add = Instruction(attr, value)
            new_handheld.instructions.append(to_add)
        return new_handheld

    """
    Gets the current instruction
    """
    def get_current_instruction(self):
        if (self.pc not in self.instructions_used and self.pc < len(self.instructions)):
            return self.instructions[self.pc]
        else:
            return None


class InstructionSet:
    def acc(state, value):
        state.instructions_used.append(state.pc)
        state.acc += value
        state.pc += 1

    def jmp(state, value):
        state.instructions_used.append(state.pc)
        state.pc += value

    def nop(state, value):
        state.instructions_used.append(state.pc)
        state.pc += 1

    table = { 
            'acc': acc,
            'jmp': jmp,
            'nop': nop
            }


class Handheld:
    # Constructor
    def __init__(self, state: HandheldState):
        self.state = state

    def execute(self):
        kill_execution = False
        while not kill_execution:
            instruction = self.state.get_current_instruction()
            if (instruction == None):
                kill_execution = True
            else:
                InstructionSet.table[instruction.attr](self.state, instruction.value)
                print(self.state)



"""
Main solution function
"""
def main_problem(input_string: str):
    new_state = HandheldState.create_instance(input_string)
    Handheld(new_state).execute()
    print(new_state.acc)

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        input_string = ""
        with open(sys.argv[1]) as f:
            input_string = f.read()
        
        main_problem(input_string)
        exit(0)
    else:
        print("Not enough arguments")

