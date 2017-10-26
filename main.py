from swarm import Swarm
from agent import Agent
from test_functions import target_function_value
from tools import prepare_move, save_plot, generate_gif, removePlots

function = "rastrigin"
agents = 150
iterations = 50
dimensions = 2
limits = [[-10,10],[-10,10]]
randomization = 0.5
attractiveness = 1.0
absorption = 0.3
save_plots = True
make_gif = True

def find_opt(test_function,number_of_agents,number_of_iterations,number_of_dimensions,area_limits, alpha, beta, gamma, save_plots, make_gif):
    The_swarm = Swarm(agents, dimensions, limits)
    Agents = The_swarm.agents

    #delete plots
    if save_plots:
        removePlots()

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
                    move = prepare_move(alpha,beta,gamma,Agents[index2].coordinates,Agents[index1].coordinates,iteration,number_of_iterations)
                    Agents[index1].move_with_vector(move)
                    Agents[index1].set_brightness(target_function_value(test_function, Agents[index1].coordinates))
        if(save_plots == True):
            save_plot([a.coordinates for a in Agents])
    
    if(make_gif == True):
        generate_gif()
    The_swarm.sort_by_brightness()
    return [Agents[0].coordinates, Agents[0].brightness]

print(find_opt(function, agents, iterations, dimensions, limits, randomization, attractiveness, absorption, save_plots, make_gif))

