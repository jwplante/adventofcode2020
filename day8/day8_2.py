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

    def clone(self):
        return Instruction(self.attr, self.value)


class HandheldState:
    # Constructor
    def __init__(self, instructions = []):
        self.instructions = instructions 
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
        if (self.pc in self.instructions_used):
            print("Infinite Loop!")
            return None
        elif self.pc >= len(self.instructions):
            print("Halted normally")
            return None
        else:
            return self.instructions[self.pc]
    
    """
    Returns a copied version of the program state with
    an instruction corrupted
    """
    def corrupt(self, number):
        inst_copy = [inst.clone() for inst in self.instructions]
        new_copy = HandheldState(inst_copy)
        if new_copy.instructions[number].attr == 'jmp':
            new_copy.instructions[number].attr = 'nop'
        elif new_copy.instructions[number].attr == 'nop':
            new_copy.instructions[number].attr = 'jmp'
        return new_copy

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
            print(instruction)
            if instruction == None:
                kill_execution = True
            else:
                InstructionSet.table[instruction.attr](self.state, instruction.value)
        
        # Detect if halted early. If so, return false.
        if self.state.pc < len(self.state.instructions):
            return False
        return True



"""
Main solution function
"""
def main_problem(input_string: str):
    base_execution = HandheldState.create_instance(input_string)
    corruptable = [x[0] for x in enumerate(base_execution.instructions) if x[1].attr == 'jmp' or x[1].attr == 'nop']

    for possible in corruptable:
        modified_state = base_execution.corrupt(possible)
        print(possible)
        if Handheld(modified_state).execute() == True:
            print(modified_state)
            return
        else:
            print(modified_state)

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        input_string = ""
        with open(sys.argv[1]) as f:
            input_string = f.read()
        
        main_problem(input_string)
        exit(0)
    else:
        print("Not enough arguments")

