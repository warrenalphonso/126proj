from array import array
import struct

bin_array = array("B") # array of ints stored in a byte

int_val = 123 
bin_array = struct.pack('i', int_val)

with open("test.bnr", "wb") as f:
    f.write(bin_array)

