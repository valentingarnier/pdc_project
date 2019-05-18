import numpy as np
import constants


def create_sinus(freq):
    array = np.zeros(constants.NUMBER_SAMPLES)
    for i in range(0, len(array)):
        array[i] = np.sin(2 * np.pi * i * (freq / constants.FREQUENCY_RATE))
    return array


def create_barker7(t):
    array = np.zeros(7 * t)
    for i in range(0, 3 * t):
        array[i] = 1
    for i in range(3 * t, 5 * t):
        array[i] = -1
    for i in range(5 * t, 6 * t):
        array[i] = 1
    for i in range(6 * t, 7 * t):
        array[i] = -1
    return array
