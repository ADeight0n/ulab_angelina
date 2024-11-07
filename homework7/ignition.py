# File: ignition.py

import numpy as np

def heating_rate(energies_gained):
    """
    Calcuates the rate at which the temperatue increases
    Input:
    2D array of the energy gained over time for different fuel tests

    Output:
    the total amount of energy gained for each fuel test
    
    """
    energy_gain = np.array([])
    

    for i in energies_gained:
        fuel_energy = 0
        for j in i:
            fuel_energy += j
        energy_gain = np.append(energy_gain, fuel_energy)

    energy_gain_rate = energy_gain/len(energies_gained)

    return energy_gain_rate
    

def energy_lost_rate(energies_lost):
    """
    Calculates the rate at which energy(the temperature) is lost
    Input:
    2D array of the energy lost over time for differnt runs

    Output:
    the total amount of energy lost during each test
    
    """
    energy_lost = np.array([])

    for i in energies_lost:
        cooling = 0
        for j in i:
            cooling += j
        energy_lost = np.append(energy_lost, cooling)

    energy_lost_rate = energy_lost/len(energies_lost)

    return energy_lost_rate
    

def achieve(eng_gain, eng_loss):
    """
    Determines if the fuel reached ignition or not by calculating the difference between energy gain and loss
    Input:

    Output:
    
    """
    energy_gained = np.array(heating_rate(eng_gain))
    energy_lost = np.array(energy_lost_rate(eng_loss))

    rate_diff = np.array(energy_gained - energy_lost)
    print(rate_diff)

    for i in range(rate_diff.size):
        index = i
        if rate_diff[index] > 0:
            print(f'run {index} achieved ignition')
        else:
            print(f'run {index} did not reach ignition')

            