import pygame

class Ship:
    """Class to take care of the spaceship"""

    def __init__(self, em_game):
        """Initializes the spaceship and defines its initial position"""
        self.screen = em_game.screen
        self.screen_rect = em_game.screen.get_rect()

        # Uploads the spaceship's image and retrieves its rect
        # I changed it, so it also handles the image transparency
        self.original_image = pygame.image.load('images/sertanejo.bmp').convert_alpha()
        o_height = self.original_image.get_height()
        o_width = self.original_image.get_width()
        scale = self.screen.get_height() / (20 * o_height)
        adjusted_size = (int(o_width * scale), int(o_height * scale))
        self.image = pygame.transform.scale(self.original_image, adjusted_size)
        self.rect = self.image.get_rect()

        # Starts each new spaceship in the bottom left of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draws the spaceship on its current position"""
        self.screen.blit(self.image, self.rect)