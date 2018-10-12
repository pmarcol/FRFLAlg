import numpy as np

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
