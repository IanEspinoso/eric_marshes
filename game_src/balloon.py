import pygamefrom pygame.sprite import Sprite

class Alien(Sprite):
    """Class to represent a single ballon in the fleet""""

    def __init__(self, em_game):
        """Initializes the ballon and defines its starting position"""
        super().__init__()
        self.screen = em_game.screen

        # Uploads the ballon image and retrieves its rect
        self.image = pygame.image.load('../misc/ballon_yel_L1.bmp')
        self.rect = self.image.get_rect()

        # Starts each new ballon near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Stores the ballon exact horizontal position
        self.x = float(self.rect.x)