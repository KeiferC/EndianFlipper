# Endian Flipper

### Description
Quick script to automate flipping bit endianness. Simple implementation.
Currently expects input to be an integer representing the number of 
bits for the expected integer representation (e.g. int16, int32) and 
a file containing hex values. 

### Usage
```shell
$ git init
$ git clone https://github.com/KeiferC/EndianFlipper.git
$ cd EndianFlipper

usage: endian-flip.py [-h] [-s <N>] <FILE>

Quick script to automate the flipping of bit endianness

positional arguments:
  <FILE>              name of file containing hex values

optional arguments:
  -h, --help          show this help message and exit
  -s <N>, --size <N>  number of bits in integer representation (default: 16).
                      Choices: [16, 32, 64]
```

### Requirements
- Python3

### Imported Modules
- sys
- argparse
