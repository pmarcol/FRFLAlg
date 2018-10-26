import numpy as np

"""
Optimization functions for algorithm testing
From: https://en.wikipedia.org/wiki/Test_functions_for_optimization
See details there (coordinates and value of global min/max)
"""

def rastrigin_function_on_arrays(coordinates, *args):
    """
    coordinates - list of arrays of the form [[xs], [ys], ...]. Particular arrays can be 1- or multicolumn (for example if mesh is needed.)
    A - steepness coefficient, if not given, then A=10 by default
    """
    largs = args[0]
    A = largs[0] if largs else 10
    sum = A*coordinates.shape[0]*np.ones(coordinates[0].shape)
    for var in coordinates:
        sum += var**2 - A*np.cos(2*np.pi*var)
    return -1.0*sum

def rosenbrock_function_on_arrays(coordinates, *args):
    # no need for additional parameters; *args just in case someone left it in algorithms' function setting.
    sum = 0
    for i in range(coordinates.shape[0]-1):
        sum += 100*(coordinates[i+1] - coordinates[i]**2)**2 + (1 - coordinates[i])**2
    return -1.0*sum

def styblinski_tang_on_arrays(coordinates, *args):
    # no need for additional parameters; *args just in case someone left it in algorithms' function setting.
    sum = 0
    for var in coordinates:
        sum += var**4 - 16.0*var**2 + 5*var
    sum = sum*(-0.5)
    return sum

