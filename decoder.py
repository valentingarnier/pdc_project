import numpy as np
import constants

def decode(frequencies):
    # decoding the sequence
    decodedBits = []
    for freq in frequencies:
        if freq <= constants.HALF_FREQ:
            decodedBits.append(-1)
        else: decodedBits.append(1)
    return decodedBits

def slicedBits(arrayBits):
    sliced = []
    for i in range(0, len(arrayBits), 8):
        sliced.append(arrayBits[i:i+8])
    return sliced


def fromBinToChar(array):
    result = ""
    for table in array:
        tableWith0 = list(map(lambda x: 0 if x == -1 else 1, table))
        string = '0b' + ''.join(map(str, tableWith0))
        n = int(string, 2)
        character = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        result = result + character
    return result
