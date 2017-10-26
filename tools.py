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

def save_plot(coordinates):
    import matplotlib.pyplot as plt
    from datetime import datetime
    xs = [item[0] for item in coordinates]
    ys = [item[1] for item in coordinates]
    axes = plt.gca()
    axes.set_xlim([-10,10])
    axes.set_ylim([-10,10])
    plt.scatter(xs,ys)
    file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    plt.savefig("plots/" + file_name + ".png")
    plt.clf()

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