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

def save_plot(coordinates, iteration, number_of_iterations):
    import matplotlib.pyplot as plt
    xs = [item[0] for item in coordinates]
    ys = [item[1] for item in coordinates]
    axes = plt.gca()
    axes.set_xlim([-6,6])
    axes.set_ylim([-6,6])
    plt.scatter(xs,ys)
    file_name = build_filename(iteration,number_of_iterations)
    plt.savefig("plots/" + file_name + ".png")
    plt.clf()

def build_filename(number, maxnumber):
    length_number = len(str(number))
    length_max = len(str(maxnumber))
    result = ""
    for dummy_i in range(length_max - length_number):
        result += "0"
    result += str(number)
    return result

def generate_gif():
    import imageio
    import glob
    files = glob.glob("plots/*.png")
    files.sort()
    images = []
    for file in files:
        images.append(imageio.imread(file))
    imageio.mimsave('gifs/animation.gif', images)