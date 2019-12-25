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
#

import sys, argparse

#########################################
# Main                                  #
#########################################
# 
# Validates input, parses command-line arguments, runs program.
#
# @param        n/a
# @returns      n/a
#
def main():
        args = parse_arguments()
        nibbles_per_word = (int) (args["size"] / 4)
        filename = args["filename"]

        hex_string = parse_infile(filename)
        hex_string = clean_hex_string(nibbles_per_word, hex_string)

        print(*flip_endian(nibbles_per_word, hex_string))
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
# @param        {int} nibbles_per_word: # of nibbles in a word
# @param        {string} hex_string: string of hex values to flip
# @returns      {list} array of flipped hex values
#
def flip_endian(nibbles_per_word, hex_string):
        words_arr = get_words(nibbles_per_word, hex_string)
        return flip_words(words_arr)

# 
# Given the number of nibbles in a word and the hex string, returns
# an array of hex words
#
# @param        {int} nibbles_per_word: # of nibbles in a word
# @param        {string} hex_string: string of hex values to parse
# @returns      {list} array of hex words
#
def get_words(nibbles_per_word, hex_string):
        words_arr = []

        for i in range(0, len(hex_string), nibbles_per_word):
                word = ""
                nibbles = 0

                while (nibbles < nibbles_per_word):
                        word += hex_string[i + nibbles]
                        nibbles += 1
                
                words_arr.append(word)
        
        return words_arr

#
# Helper to flip_endian. Given an array of words, reverse the order
# of the bytes in each word.
#
# @param        {list} words_arr: array of hex words
# @returns      {list} an array of flipped hex words
#
def flip_words(words_arr):
        flipped_arr = []

        for word in words_arr:
                flipped_word = ""

                for nibble in range(len(word) - 1, 0, -2):
                        flipped_word += (word[nibble - 1] + word[nibble])
                
                flipped_arr.append(flipped_word)

        return flipped_arr

#
# Given the number of nibbles per word and a hex string, prepends
# a buffer of zeros to ensure a divisible number of bits according
# to the established integer representation
#
# @param        {int} nibbles_per_word: # of nibbles per word
# @param        {string} hex_string: string of hex values to clean
# @returns      {string} hex_string prepended with zeros buffer
#
def clean_hex_string(nibbles_per_word, hex_string):
        length = len(hex_string)
        offset = (int) (length % nibbles_per_word)
        zeros_buffer = 0

        if (offset != 0):
                zeros_buffer = nibbles_per_word - offset
        
        return hex_string.zfill(length + zeros_buffer)


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
# @returns      {string} string of hex values to flip
#
def parse_infile(filename):
        hex_string = ""

        try:
                with open(filename, 'r') as file:
                        for line in file:
                                for word in line.split():
                                        hex_string += word
        except FileNotFoundError:
                print("No such file \'{}\' in directory.".format(filename))
                sys.exit("Error: FileNotFoundError.")
        except:
                print("Unable to open file \'{}\'.".format(filename))
                sys.exit("Error: Unable to open file.")

        return hex_string


#########################################
# Function Calls                        #
#########################################
if __name__ == "__main__":
        main()
