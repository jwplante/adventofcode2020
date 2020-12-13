# Advent of Code 2020 Day 4-1
# James Plante

import sys
import string
import re


"""
Class that represents a Passport in an airport
@author James Plante (jplante@wpi.edu)
"""
class Passport:
    
    # Constructor (DO NOT CALL ON OWN)
    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None
    
    """
    Factory method to create a Passport object based on a string
    with the format field:value. Fields can be separated by either
    spaces or newlines.
    @param passport_string - String with fields
    """
    def instance_from_string(passport_string):
        new_factory = Passport()
        field_list = re.split("[\n, ]", passport_string)
        
        # Using a list comprehension to get rid of empty strings
        for field in [x for x in field_list if x != '']:
            key, value = field.split(':')
            setattr(new_factory, key, value)

        return new_factory

    """
    Returns true if the Passport is Valid.
    (i.e.) if all fields are there except for cid.
    """
    def isValid(self):
        return (
                self.byr != None and
                self.iyr != None and
                self.eyr != None and
                self.hgt != None and
                self.hcl != None and
                self.ecl != None and
                self.pid != None
                )

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        input_string = ""
        with open(sys.argv[1]) as f:
            input_string = f.read()

        counter = 0    
        for passport_string in input_string.split('\n\n'):
            if (passport_string != ''):
                if (Passport.instance_from_string(passport_string).isValid()):
                    counter += 1
        print(counter)
        exit(0)
    else:
        print("Not enough arguments")

