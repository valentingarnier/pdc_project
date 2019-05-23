import numpy as np
import cutting
import constants

only_data = cutting.cuttingData()

dataSliced = []
for i in range(5, len(only_data), 100):
    if i + 90 > len(only_data):
        break
    dataSliced.append(only_data[i: i + 90])
    print(len(only_data[i: i + 90]))
print("this is datasliced", dataSliced, "\n")

dataSlicedF = []
freqs = []

for i, line in enumerate(dataSliced):
    dataSlicedF[i] = np.fft.rfft(line)
    freqs[i] = np.fft.fftfreq(len(line))

# Find the peak in the coefficients
dataSlicedFClean = []
for i, line in enumerate(dataSlicedF):
    idx = np.argmax(np.abs(line))
    freq = freqs[idx]
    dataSlicedFClean[i] = abs(freq * constants.FREQUENCY_RATE) #freq in hertz


decodedBits = []
for idx, freq in enumerate(dataSlicedFClean):
    if freq >= 0 and freq <= constants.HALF_FREQ:
        decodedBits[idx] = -1
    else: decodedBits[idx] = 1
