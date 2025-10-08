import pygame
from pygame.sprite import Sprite

class Bead(Sprite):
    """Class to manage beads launched by the hero"""

    def __init__(self, em_game):
        """Generates a bead object at the hero's current position"""
        super().__init__()
        self.screen = em_game.screen
        self.settings = em_game.settings
        self.color = self.settings.bead_color

        # Creates a bead in (0, 0) and, right away, define the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bead_width,
                                self.settings.bead_height)
        self.rect.topright = em_game.sertanejo.rect.topright

        # Saves the bead's position as a float
        self.y = float(self.rect.y)

    def update(self):
        """Vertically displaces the bead across the screen"""
        # Updates the bead's exact position
        self.y -= self.settings.bead_speed
        # Updates the rect's position
        self.rect.y = self.y

    def draw_bead(self):
        """Draws the bead on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
