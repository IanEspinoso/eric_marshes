import pygame 
from pygame.sprite import Sprite

class Balloon(Sprite):
    """Class to represent a single ballon in the fleet"""

    def __init__(self, em_game):
        """Initializes the ballon and defines its starting position"""
        super().__init__()
        self.screen = em_game.screen
        self.settings = em_game.settings

        # Uploads the ballon image and retrieves its rect
        self.original_image = pygame.image.load('../misc/balloons/yel.bmp')
        o_height = self.original_image.get_height()
        o_width = self.original_image.get_width()
        scale = self.screen.get_height() / (30 * o_height)
        adjusted_size = (int(o_width * scale), int(o_height * scale))
        self.image = pygame.transform.scale(self.original_image, adjusted_size)
        self.rect = self.image.get_rect()

        # Starts each new ballon near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Stores the ballon exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Returns True if the ballon is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right or self.rect.left <= 0)
    
    def update(self):
        """Moves the ballon to the right"""
        self.x += self.settings.balloon_speed * self.settings.fleet_direction
        self.rect.x = self.x