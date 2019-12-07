import struct 

with open("test.bnr", "rb") as f:
    print(struct.unpack("i", f.read(4)))
