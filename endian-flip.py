#
#       filename:       endian-flip.py
#       author:         @KeiferC
#       date:           24 Dec 2019
#       version:        0.0.1
#       
#       description:    Quick script to automate flipping bit
#                       endianness
#
#       usage:          python endian-flip.py [-h] [-s <N>] <FILE>
#
#       TODO:           - Input type option (currently default to hex)
#                       - Input type validation
#                       - Binary conversion (output)
#                       - Decimal conversion (output)
#                       - ASCII conversion (output)
#                       - Robust num bits testing
#

import sys, argparse

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
        args = parse_arguments()
        int_size = args["size"]
        filename = args["filename"]
        hex_arr = parse_infile(filename)
        
        print(*flip_endian(int_size, hex_arr), sep=",")
        sys.exit()


#########################################
# Functions                             #
#########################################
#
# Given a dictionary containing a number of bits for an integer
# representation and an array of hex values, flips endianness of hex 
# values in accordance with the integer representation. Returns an array 
# of flipped hex values.
#
# @param        {int} int_size: # bits for int representation
#               {list} hex_arr: array of hex values to flip
# @return       {list} array of flipped hex values
#
def flip_endian(int_size, hex_arr):
        # TODO

        return hex_arr


#########################################
# Command-Line Parsing                  #
#########################################
#
# Parses command-line arguments and returns a dictionary of argument
# objects
#
# @param        n/a
# @returns      {dictionary} Contains following key-value pairs:
#                       {string} filename: name of file to parse
#                       {int} size: # of bits for int representation
#
def parse_arguments():
        description = "Quick script to automate the flipping of bit endianness"
        file_help = "name of file containing hex values"
        size_help = "number of bits in integer representation (default: 16). \
                Choices: [16, 32, 64]"

        parser = argparse.ArgumentParser(description=description)

        parser.add_argument("filename", metavar="<FILE>", help=file_help)
        parser.add_argument("-s", "--size", dest="size", metavar="<N>", 
                type=int, choices=[16, 32, 64], default=16, help=size_help)

        return vars(parser.parse_args())

#
# Given a filename, opens file and returns an array of hex values to flip
#
# @param        {string} filename: file to open
# @returns      {list} array of hex values to flip
#
def parse_infile(filename):
        hex_arr = []

        with open(filename, 'r') as file:
                for line in file:
                        for word in line.split():
                                hex_arr.append(word)

        return hex_arr


#########################################
# Function Calls                        #
#########################################
if __name__ == "__main__":
        main()
