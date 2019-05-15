import numpy as np

def encode(str):
    intForm = int.from_bytes(string.encode('ascii'), byteorder='big', signed = True)
    binaryForm = bin(intForm)
    result = binaryForm[2:]
    result = [int(x) for x in result]
    result = [-1] + list(map(lambda x: -1 if x == 0 else 1, result)) #if we consider that 0 is equivalent to -1 in binary
    return result
