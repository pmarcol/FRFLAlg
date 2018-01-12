import random
import math

def add_vectors(list1, list2):
    "Allows to add two lists vector-like"
    final_list = []
    if len(list1) != len(list2):
        print("Length of the first array does not match length of the second one.")
        return

    for i in range(len(list1)):
        final_list.append(list1[i] + list2[i])

    return final_list

def subtract_vectors(list1, list2):
    "Allows to subtract two lists vector-like"
    final_list = []
    if len(list1) != len(list2):
        print("Length of the first array does not match length of the second one.")
        return

    for i in range(len(list1)):
        final_list.append(list1[i] - list2[i])

    return final_list

def scalar_multiply(value, list):
    final_list = []
    for i in range(len(list)):
        final_list.append(value*list[i])
    
    return final_list

def prepare_agent(limits):
    "Prepares agent with random coordinates matching given limits"
    agent = []
    for limit_pair in limits:
        agent.append(random.uniform(limit_pair[0], limit_pair[1]))
    return agent

def euclidean_distance(list1, list2):
    "Allows to calculate the euclidean distance between to vectors"
    sum = 0
    for i in range(len(list1)):
        sum += (list1[i] - list2[i])**2
    return math.sqrt(sum)

def prepare_move(alpha, beta, gamma, coords_attracting, coords_attracted, iteration, number_of_iterations):
    #non-random part
    azimuth = subtract_vectors(coords_attracting, coords_attracted)
    distance = euclidean_distance(coords_attracted, coords_attracting)
    coefficient = beta * math.exp((-1.0) * gamma * distance**2)
    non_random_move = scalar_multiply(coefficient, azimuth)
    #random part
    vibration = (number_of_iterations - iteration)/number_of_iterations
    random_move = []
    for dummy_i in range(len(coords_attracting)):
        random_move.append(alpha*random.uniform(-vibration, vibration))
    #assembling result
    final_move = add_vectors(non_random_move, random_move)
    return final_move

def generate_gif():
    import imageio
    import glob
    import time
    files = glob.glob("plots/*.png")
    files.sort()
    images = []
    for file in files:
        images.append(imageio.imread(file))
    timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
    imageio.mimsave('gifs/%s.gif' % timestr, images, duration = .5)

def removePlots():
    import glob
    import os

    plotsPath = "plots/*.png"
    files = glob.glob(plotsPath)

    for f in files:
        os.remove(f)

def removeGifs():
    import glob
    import os

    plotsPath = "gifs/*.gif"
    files = glob.glob(plotsPath)

    for f in files:
        os.remove(f)
        
def prepare_heatmap_table(xrange, yrange, resolution, function):
    import numpy as np
    from test_functions import target_function_value
    output_table = []
    xstep = (xrange[1] - xrange[0])/resolution
    ystep = (yrange[1] - yrange[0])/resolution
    xs = []
    ys = []
    for i in range(resolution + 1):
        xs.append(xrange[0] + i*xstep)
        ys.append(yrange[0] + i*ystep)
    X, Y = np.meshgrid(xs, ys)
    output_table.append(X)
    output_table.append(Y)
    vals = np.zeros_like(X)
    for i in range(len(vals[0])):
        for j in range(len(vals)):
            vals[i, j] = target_function_value(function, [X[i, j], Y[i, j]])
    output_table.append(vals)
    return output_table