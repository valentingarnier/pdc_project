import numpy as np

def encodeChar(c):
    intForm = int.from_bytes(c.encode('ascii'), byteorder='big') #cette fonction marche seulement bien pour les caracteres
    binaryForm = bin(intForm)
    result = binaryForm[2:]
    result = [-1]*(8-len(result)) + list(map(lambda x: -1 if x == '0' else 1, result)) #if we consider that 0 is equivalent to -1 in binary
    return result

def encode(str):
    encodedString = []
    for char in str:
        encodedString = np.concatenate((encodedString, encodeChar(char)))

    print("encoded sequence: ", encodedString)
    return encodedString
