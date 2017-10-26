import math

def target_function_value(func_string, argument):
    "Returns value of one of the defined functions (func_string, available: \"rastrigin\" for argument given as list"
    switcher = {
        "rastrigin" : rastrigin_function
    }

    func = switcher.get(func_string)
    return func(argument)

def rastrigin_function(argument):
    "Rastrigin test function"
    A = 10
    n = len(argument)
    sum = 0
    for i in range(n):
        sum += argument[i]**2 - A*math.cos(2*math.pi*argument[i])
    
    sum += A*n
    return -1.0 * sum
