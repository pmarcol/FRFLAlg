import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class ConvergenceVisualization:
    """
    Class implementing the visualization tool for the Firefly Algorithm.
    """

    def __init__(self, bounds_x, bounds_y):
        self.populations = []
        self.animation = None
        self.heatmap_table = None
        self.xrange = bounds_x
        self.yrange = bounds_y

    def generate_heatmap_table(self, resolution, function, f_args={}):
        """
        f_args - any additional parameters needed to calculate the target function
        """
        output_table = []
        xs = np.linspace(self.xrange[0], self.xrange[1], resolution)
        ys = np.linspace(self.yrange[0], self.yrange[1], resolution)
        X, Y = np.meshgrid(xs, ys)
        output_table.append(X)
        output_table.append(Y)
        vals = np.zeros(X.shape)
        vals = function(np.array([X, Y]), f_args)
        output_table.append(vals)
        self.heatmap_table = output_table
        self.sct = None

    def append_population(self, pop):
        self.populations.append(pop)

    def generate_animation(self):
        xs = self.populations[0][:,0]
        ys = self.populations[0][:,1]
        self.fig = plt.figure()
        self.fig.gca().set_aspect('equal', adjustable='box')
        plt.pcolormesh(self.heatmap_table[0], self.heatmap_table[1], self.heatmap_table[2])
        self.sct = plt.scatter(xs, ys, marker = '*', c = 'tab:orange')
        self.animation = FuncAnimation(self.fig, self.update, frames=range(len(self.populations)))

    def update(self, i):
        xs = self.populations[i][:,0]
        ys = self.populations[i][:,1]
        xys = np.transpose(np.array([xs, ys]))
        self.sct.set_offsets(xys)
        self.fig.set_label("iteration: {0}".format(i))
        return self.sct
