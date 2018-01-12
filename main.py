from swarm import Swarm
from test_functions import target_function_value
from tools import prepare_move, generate_gif, removePlots, prepare_heatmap_table

function = "rastrigin"
agents = 50
iterations = 50
dimensions = 2
limits = [[-10,10],[-10,10]]
randomization = 0.5
attractiveness = 1.0
absorption = 0.3
save_plots = True
add_heatmap = True
heatmap_table = None
heatmap_resolution = 1000
make_gif = True

def find_opt(test_function,number_of_agents,number_of_iterations,number_of_dimensions,area_limits, alpha, beta, gamma):#, save_plots, make_gif):
    The_swarm = Swarm(agents, dimensions, limits)
    Agents = The_swarm.agents
    global heatmap_table

    #delete plots
    if save_plots:
        removePlots()
        
    #prepare heatmap table
    if add_heatmap:
        heatmap_table = prepare_heatmap_table(limits[0], limits[1], heatmap_resolution, test_function)

    #Set the brightness across the swarm
    for single_agent in Agents:
        single_agent.set_brightness(target_function_value(test_function, single_agent.coordinates))
    
    #loop for iterations
    for iteration in range(number_of_iterations):
        #loops for agents in swarm
        for index1 in range(number_of_agents):
            for index2 in range(number_of_agents):
                if index1 == index2:
                    continue
                if not Agents[index2].brightness > Agents[index1].brightness:
                    continue
                else:
                    #the part, where one agent moves towards another
                    move = prepare_move(alpha,
                                        beta,
                                        gamma,
                                        Agents[index2].coordinates,
                                        Agents[index1].coordinates,
                                        iteration,number_of_iterations)
                    Agents[index1].move_with_vector(move)
                    Agents[index1].set_brightness(
                          target_function_value(test_function,
                                                Agents[index1].coordinates)
                          )
        if(save_plots):
            save_plot([a.coordinates for a in Agents], area_limits[0], area_limits[1], add_heatmap, heatmap_resolution)
    
    if(make_gif):
        generate_gif()
    The_swarm.sort_by_brightness()
    return [Agents[0].coordinates, Agents[0].brightness]


def save_plot(coordinates, xrange, yrange, heatmap, resolution):
    import matplotlib.pyplot as plt
    from datetime import datetime
    xs = [item[0] for item in coordinates]
    ys = [item[1] for item in coordinates]
    axes = plt.gca()
    cir = plt.Circle((0, 0), 1.0, color='r', fill=False)
    axes.set_xlim(xrange)
    axes.set_ylim(yrange)
    axes.add_artist(cir)
    if heatmap:
        plt.pcolormesh(heatmap_table[0], heatmap_table[1], heatmap_table[2])
    plt.scatter(xs, ys, marker = '*', c = 'tab:orange')
    file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    plt.savefig("plots/" + file_name + ".png")
    plt.clf()

print(find_opt(function, agents, iterations, dimensions, limits, randomization, attractiveness, absorption))#, save_plots, make_gif))

