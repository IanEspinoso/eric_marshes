import pygame

class Ship:
    """Class to take care of the spaceship"""

    def __init__(self, ai_game):
        """Initializes the spaceship and defines its initial position"""
        self.screen = ai_game.screen
        slef.screen_rect = ai_game.screen.get_rect()

        # Uploads the spaceship's image and retrieves its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Starts each new spaceship in the bottom left of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draws the spaceship on its current position"""
        self.screen.blit(self.image, self.rect)