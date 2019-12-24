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
$ python endian-flip.py [-h] [-s <N>] <FILE>
```

### Requirements
- Python3

### Imported Modules
- sys
- argparse
