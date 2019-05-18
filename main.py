import numpy as np
import constants
import encoder
import waveformer

string = "h"
result = waveformer.create_barker7(2)
for bit in encoder.encode(string):
    if bit == -1:
        array1 = waveformer.create_sinus(constants.FREQUENCY_0_1)
        array2 = waveformer.create_sinus(constants.FREQUENCY_0_2)
        result = np.concatenate((result, (array1 + array2)/2)).astype(np.float32)
    else:
        array1 = waveformer.create_sinus(constants.FREQUENCY_1_1)
        array2 = waveformer.create_sinus(constants.FREQUENCY_1_2)
        result = np.concatenate((result, (array1 + array2)/2)).astype(np.float32)

result = np.concatenate((result, waveformer.create_barker7(2))).astype(np.float32)


for i in result:
    print(i)
