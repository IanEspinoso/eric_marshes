from random import choice

class RandomWalk:
    """ Class to generate random walks """

    def __init__(self, num_points=5000):
        """ Initializes the walks attributes """
        self.num_points = num_points
        
        # All the walks begin at (0, 0)
        self.x_values = [0]
        self.y_values = [0]