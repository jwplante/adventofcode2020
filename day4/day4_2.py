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
    def instance_from_string(passport_string: str):
        new_passport = Passport()
        field_list = re.split("[\n, ]", passport_string)
        
        # Using a list comprehension to get rid of empty strings
        for field in [x for x in field_list if x != '']:
            key, value = field.split(':')
            setattr(new_passport, key, value)

        return new_passport

    """
    Returns true if the fields in the Passport are initialized.
    (i.e.) if all fields are there except for cid.
    """
    def is_initialized(self):
        return (
                self.byr != None and
                self.iyr != None and
                self.eyr != None and
                self.hgt != None and
                self.hcl != None and
                self.ecl != None and
                self.pid != None
                )

    """
    Returns true if the passport is valid based on the Passport's
    parameters based on these rules:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    def is_valid(self):

        # Returns true if string integer is within the range [top, bottom]
        def number_parameter_in_range(value: str, bottom: int, top: int):
            try:
                integer = int(value)
                return integer >= bottom and integer <= top
            except:
                print("Cannot parse integer!")
                return False
        
        # Returns true if the string integer is a valid measurement
        def valid_height(value: str):
            measurement_limits = {'in': (59, 76), 'cm': (150, 193)}
            if re.fullmatch("[0-9]+in|[0-9]+cm", value) != None:
                scalar = int(value[:-2])
                unit = value[-2:]
                return scalar >= measurement_limits[unit][0] and scalar <= measurement_limits[unit][1]
            return False
                    
        
        # Returns true if the string is an sRGB value
        def is_rgb(value: str):
            return re.fullmatch("#[0-9a-f]{6}", value) != None
        
        # Returns true if the string is a valid eye color
        def valid_eye_color(value: str):
            eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            return value in eye_colors

        # Returns true if the string integer is num_digits digits long
        def number_is_x_digits(value: str, num_digits: int):
            try:
                int(value) ## Will throw an exception if it is not an integer
                return len(value) == num_digits
            except:
                return False

        if (self.is_initialized()):
            return (
                    number_parameter_in_range(self.byr, 1920, 2002) and
                    number_parameter_in_range(self.iyr, 2010, 2020) and
                    number_parameter_in_range(self.eyr, 2020, 2030) and
                    valid_height(self.hgt) and
                    is_rgb(self.hcl) and
                    valid_eye_color(self.ecl) and
                    number_is_x_digits(self.pid, 9)
                    )
        else:
            return False


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        input_string = ""
        with open(sys.argv[1]) as f:
            input_string = f.read()

        counter = 0    
        for passport_string in input_string.split('\n\n'):
            if (passport_string != ''):
                if (Passport.instance_from_string(passport_string).is_valid()):
                    counter += 1
        print(counter)
        exit(0)
    else:
        print("Not enough arguments")

