import numpy as np
import constants

def create_sinus(freq):
    array = np.zeros(constants.NUMBER_SAMPLES)
    for i in range(0, len(array)):
        array[i] = np.sin(2*np.pi*i*(freq/constants.FREQUENCY_RATE))
    return array
