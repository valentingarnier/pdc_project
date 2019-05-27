import numpy as np
import constants

def decode(frequencies):
    # decoding the sequence
    decodedBits = np.empty((constants.SIZE_OF_ENCODED_SEQUENCE, ))
    for idx, freq in enumerate(frequencies):
        if freq <= constants.HALF_FREQ:
            decodedBits[idx] = -1
        else: decodedBits[idx] = 1
    return decodedBits

def decode8bits(arrayBits):
    return None
