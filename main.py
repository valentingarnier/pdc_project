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

#Initialization of arrays
dataSlicedF = []
freqs = []

for line in dataSliced:
    dataSlicedF.append(np.fft.rfft(line))
    freqs.append(np.fft.fftfreq(len(line)))

# Find the peak in the coefficients
dataSlicedFClean = []
for i, line in enumerate(dataSlicedF):
    idx = np.argmax(np.abs(line))
    freq = freqs[i][idx]
    dataSlicedFClean.append(abs(freq * constants.FREQUENCY_RATE)) #freq in hertz

decodedBits = decoder.decode(dataSlicedFClean)

cutted = decoder.slicedBits(np.asarray(decodedBits))
finalText = decoder.fromBinToChar(cutted)

finalOutput = open("output.txt", "w")
finalOutput.write(finalText)
