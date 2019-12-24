#
#       filename:       endian-flip.py
#       author:         @KeiferC
#       date:           24 Dec 2019
#       version:        0.0.1
#       
#       description:    Quick script to automate flipping bit
#                       endianness
#
#       usage:          python xmlparser.py -s <integer_size> <FILE>
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
# main
#
# Validates input, parses command-line arguments, runs program.
#
# @param        n/a
# @return       n/a
#
def main():
        # TODO

        if (valid_input()):
                flip(parse())
                sys.exit()
        else:
                usage()
                sys.exit("Usage error")


#########################################
# Functions                             #
#########################################
# 
# flip_endian
#
# Given a dictionary containing a number of bits for an integer
# representation and an array of hex values, flips endianness of  the hex 
# values in accordance with the integer representation. Returns an array 
# of flipped hex values
#
# @param        {dictionary} flipper_args: contains the following kv-pairs
#                       {number} int_size: # bits for int representation
#                       {list} hex_arr: array of hex values to flip
# @return       {list} array of flipped hex values
#
def flip_endian(flipper_args):
        # TODO

        return None


#
# TODO
#
def valid_input():
        # TODO

        return True


#
# TODO
#
def parse():
        # TODO

        flipper_args = {"num_bits": None, "hex_arr": None}
        return flipper_args


#########################################
# Function Calls                        #
#########################################
if __name__ == "__main__":
        main()
