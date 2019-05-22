import numpy as np
import constants
import encoder
import waveformer


with open("input.txt") as file:
    string = file.readlines()
string = [x.strip() for x in string]

result = []
result = waveformer.create_barker7(1)
for bit in encoder.encode(string):
    if bit == -1:
        array1 = waveformer.create_sinus(constants.FREQUENCY_0_1)
        array2 = waveformer.create_sinus(constants.FREQUENCY_0_2)
        result = np.concatenate((result, (array1 + array2)/4)).astype(np.float32)
    else:
        array1 = waveformer.create_sinus(constants.FREQUENCY_1_1)
        array2 = waveformer.create_sinus(constants.FREQUENCY_1_2)
        result = np.concatenate((result, (array1 + array2)/4)).astype(np.float32)

result = np.concatenate((result, waveformer.create_barker7(1))).astype(np.float32)

input_file = open("input.txt", "w+")
result = [str(x) for x in result]
for s in result:
    input_file.write(s+"\n")
