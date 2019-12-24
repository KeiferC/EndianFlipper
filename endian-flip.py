#
#       filename:       endian-flip.py
#       author:         @KeiferC
#       date:           24 Dec 2019
#       version:        0.0.1
#       
#       description:    Quick script to automate flipping bit
#                       endianness
#
#       usage:          python endian-flip.py -s <integer_size> <FILE>
#
#       TODO:           - Input type option (currently default to hex)
#                       - Input type validation
#                       - Binary conversion (output)
#                       - Decimal conversion (output)
#                       - ASCII conversion (output)
#                       - Robust num bits testing
#

import sys

#########################################
# Main                                  #
#########################################
# 
# Validates input, parses command-line arguments, runs program.
#
# @param        n/a
# @return       n/a
#
def main():
        if (valid_input()):
                print(*flip_endian(parse_infile()))
                sys.exit()
        else:
                usage()
                sys.exit("Usage error")


#########################################
# Functions                             #
#########################################
# 
# Given a dictionary containing a number of bits for an integer
# representation and an array of hex values, flips endianness of hex 
# values in accordance with the integer representation. Returns an array 
# of flipped hex values.
#
# @param        {dictionary} flipper_args: contains the following kv-pairs
#                       {number} int_size: # bits for int representation
#                       {list} hex_arr: array of hex values to flip
# @return       {list} array of flipped hex values
#
def flip_endian(flipper_args):
        # TODO

        return ["test", "one"]


#########################################
# Command-Line Parsing                  #
#########################################
#
# Returns true if the command-line arguments are valid. Currently not 
# robust at all for speedy scripting and use.
#
# @param        n/a
# @returns      {boolean} True if arguments are valid
#
def valid_input():
        # TODO

        return True

#
# Retrieves command-line arguments from system and parses given file
# accordingly. Returns a dictionary containing integer representation
# and array of hex values from file.
#
# @param        n/a
# @returns      {dictionary} flipper_args: contains the following kv-pairs
#                       {number} int_size: # bits for int representation
#                       {list} hex_arr: array of hex values to flip
#
def parse_infile():
        # TODO

        flipper_args = {"num_bits": None, "hex_arr": None}
        return flipper_args


#########################################
# Function Calls                        #
#########################################
if __name__ == "__main__":
        main()
