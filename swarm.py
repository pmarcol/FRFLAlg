from tools import prepare_agent
from agent import Agent

class Swarm:
    
    agents = []

    def __init__(self, number_of_agents, number_of_dimensions, dimensions_limits):
        if len(dimensions_limits) != number_of_dimensions:
            print("Number of dimensions does not match the number of dimensions in limits array")
            return

        for dummy_index in range(number_of_agents):
            temp_agent = Agent(prepare_agent(dimensions_limits))
            self.agents.append(temp_agent)
        return

    def sort_by_brightness(self):
        "Sorts the swarm by brightness of its agents"
        self.agents.sort(key = lambda x: x.brightness, reverse=True)
        return

