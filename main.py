from swarm import Swarm
from agent import Agent
from test_functions import target_function_value
from tools import prepare_move
from tools import save_plot
from tools import generate_gif

function = "rastrigin"
agents = 70
iterations = 30
dimensions = 2
limits = [[-10,10],[-10,10]]
randomization = 0.5
attractiveness = 1.0
absorption = 0.3
save_plots = True
make_gif = True

def find_opt(test_function,number_of_agents,number_of_iterations,number_of_dimensions,area_limits, alpha, beta, gamma):
    the_swarm = Swarm(agents, dimensions, limits)
    #Set the brightness across the swarm
    for single_agent in the_swarm.agents:
        single_agent.set_brightness(target_function_value(test_function, single_agent.coordinates))
    
    #loop for iterations
    for iteration in range(number_of_iterations):
        #loops for agents in swarm
        for index1 in range(number_of_agents):
            for index2 in range(number_of_agents):
                if index1 == index2:
                    continue
                if not the_swarm.agents[index2].brightness > the_swarm.agents[index1].brightness:
                    continue
                else:
                    #the part, where one agent moves towards another
                    move = prepare_move(alpha,beta,gamma,the_swarm.agents[index2].coordinates,the_swarm.agents[index1].coordinates,iteration,number_of_iterations)
                    the_swarm.agents[index1].move_with_vector(move)
                    the_swarm.agents[index1].set_brightness(target_function_value(test_function, the_swarm.agents[index1].coordinates))
        if(save_plots == True):
            save_plot([a.coordinates for a in the_swarm.agents],iteration+1,number_of_iterations)
    
    the_swarm.sort_by_brightness()
    return [the_swarm.agents[0].coordinates, the_swarm.agents[0].brightness]

print(find_opt(function, agents, iterations, dimensions, limits, randomization, attractiveness, absorption))
if(make_gif == True):
    generate_gif()
    print("GIF file succesfully saved!")
