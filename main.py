import numpy as np
import cutting
import constants
import decoder

only_data = cutting.cuttingData()

dataSliced = []
for i in range(5, len(only_data), constants.NUMBER_SAMPLES):
    if i + (constants.NUMBER_SAMPLES - 10) > len(only_data):
        break
    dataSliced.append(only_data[i: i + (constants.NUMBER_SAMPLES - 10)])

#Sizes of arrays
numberOfElemDataSlicedF = len(np.fft.rfft(dataSliced[0]))
numberOfElemFreqs = len(np.fft.fftfreq(len(dataSliced[0])))

#Initialization of arrays
dataSlicedF = np.empty((constants.SIZE_OF_ENCODED_SEQUENCE, numberOfElemDataSlicedF))
freqs = np.empty((constants.SIZE_OF_ENCODED_SEQUENCE, numberOfElemFreqs))

for i, line in enumerate(dataSliced):
    dataSlicedF[i] = np.fft.rfft(line)
    freqs[i] = np.fft.fftfreq(len(line))

# Find the peak in the coefficients
dataSlicedFClean = np.empty((constants.SIZE_OF_ENCODED_SEQUENCE, 1))
for i, line in enumerate(dataSlicedF):
    idx = np.argmax(np.abs(line))
    freq = freqs[i][idx]
    dataSlicedFClean[i] = abs(freq * constants.FREQUENCY_RATE) #freq in hertz

decodedBits = decoder.decode(dataSlicedFClean)

print("this is the decoded sequence: ", decodedBits[: len(decodedBits) - 1])
