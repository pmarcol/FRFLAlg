import numpy as np
import itertools as it
from visualization import ConvergenceVisualization

class FireflyAlgorithm:
    """
    Class implementing the Firefly Optimization Algorithm.
    Default values of parameters:
    number of iterations: 50
    number of agents: 50
    alpha (randomness): 0.5
    beta (atractiveness): 1.0
    gamma (light absorption): 0.3
    visualization_resolution: 1000
    """

    def __init__(self):
        self.f = None
        self.f_args = None
        self.boundaries = None
        self.number_of_iterations = 50
        self.number_of_agents = 50
        self.alpha = 0.5
        self.beta = 1.0
        self.gamma = 0.3
        self.visualize = False
        self.best_agent = None
        self.best_score = None
        self.visualization = None
        self.visualization_resolution = 1000

    def set_function(self, func, *args):
        "Sets the function to be optimized. args are optional parameters for target function"
        self.f = func
        self.f_args = args if args else None

    def set_boundaries(self, bounds):
        """
        Sets the boundaries in which the optimum will be searched for.
        Format: list of form [[x_bottom, x_top], [y_bottom, y_top], ...]
        Note: This method also defines dimensionality of the investigated space!
        """
        self.boundaries = np.array(bounds)

    def set_number_of_iterations(self, iters):
        "Sets the number of iterations for the algorithm. Default = 50"
        self.number_of_iterations = iters

    def set_number_of_agents(self, agents):
        "Sets the number of agents for the algorithm. Default = 50"
        self.number_of_agents = agents

    def set_alpha(self, alpha):
        self.alpha = alpha

    def set_beta(self, beta):
        self.beta = beta
    
    def set_gamma(self, gamma):
        self.gamma = gamma

    def set_generate_visualization(self, visualize):
        "Bool; should visualization be generated? Note: available only for 2-arguments target functions."
        self.visualize = visualize

    def set_visualization_resolution(self, res):
        self.visualization_resolution = res

    def get_best_agent(self):
        return self.best_agent

    def get_best_score(self):
        return self.best_score

    def run(self):
        if self.boundaries is None:
            print("The boundaries were not set!")
            return
        dims = self.boundaries.shape[0]
        pairs = list(it.combinations(range(self.number_of_agents), 2))
        pop = self.prepare_population(self.boundaries, self.number_of_agents)
        vals = self.f(np.array([pop[:,c] for c in range(dims)]), self.f_args)
        bottom_bounds = np.zeros(pop.shape)
        top_bounds = np.zeros(pop.shape)
        for c in range(dims):
            bottom_bounds[:,c] = self.boundaries[c][0]
            top_bounds[:,c]= self.boundaries[c][1]
        if self.visualize and dims == 2:
            self.visualization = ConvergenceVisualization(self.boundaries[0], self.boundaries[1])
            self.visualization.generate_heatmap_table(
                self.visualization_resolution,
                self.f,
                self.f_args)
            self.visualization.append_population(pop)

        for _ in range(self.number_of_iterations):
            for pair in pairs:
                if vals[pair[0]] > vals[pair[1]]:
                    gr = pair[0]
                    sm = pair[1]
                else:
                    gr = pair[1]
                    sm = pair[0]
                move = self.prepare_move(self.alpha, self.beta, self.gamma, pop[gr], pop[sm])
                pop[sm] += move
                pop = np.clip(pop, bottom_bounds, top_bounds)
                vals[sm] = self.f(np.array([pop[sm, c] for c in range(dims)]), self.f_args)
            if self.visualize and dims==2:
                self.visualization.append_population(pop)
        
        ord = vals.argsort()
        pop = pop[ord[::-1]]
        vals = vals[ord[::-1]]
        self.best_agent = pop[0]
        self.best_score = vals[0]

    def prepare_population(self, bounds, n):
        dims = bounds.shape[0]
        out = np.zeros((n, dims))
        for c in range(dims):
            out[:,c] = np.random.uniform(bounds[c,0], bounds[c,1],n)
        return out

    def prepare_move(self, alpha, beta, gamma, gr_coordinates, sm_coordinates):
        dims = gr_coordinates.shape[0]
        azimuth = gr_coordinates - sm_coordinates
        distance = np.linalg.norm(gr_coordinates - sm_coordinates)
        coefficient = beta * np.exp((-1.0) * gamma * distance**2)
        non_random_part = coefficient*azimuth
        #random part
        random_part = alpha*np.random.uniform(-1.0, 1.0, dims)
        #assembling result
        final_move = non_random_part + random_part
        return final_move

