from random import randint
class Die:
    """ Class to represent a single die """

    def __inet__(self, num_sides=6):
        """ Makes the supposition that a die has six sides """
        self.num_sides = num_sides

    def roll(self):
        """ Returns a random value between 1 and the number of sides """
        return randint(1, self.num_sides)