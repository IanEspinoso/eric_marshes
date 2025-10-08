import pygame

class Sertanejo:
    """Class to manage the sertanejo"""

    def __init__(self, em_game):
        """Initializes the sertanejo and defines its initial position"""
        self.screen = em_game.screen
        self.settings = em_game.settings
        self.screen_rect = em_game.screen.get_rect()

        # Uploads the sertanejo's image and retrieves its rect
        # I changed it, so it also handles the image transparency
        self.original_image = pygame.image.load('../misc/sertanejo_dark_L1.bmp').convert_alpha()
        o_height = self.original_image.get_height()
        o_width = self.original_image.get_width()
        scale = self.screen.get_height() / (20 * o_height)
        adjusted_size = (int(o_width * scale), int(o_height * scale))
        self.image = pygame.transform.scale(self.original_image, adjusted_size)
        self.rect = self.image.get_rect()

        # Starts each new sertanejo in the middle bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Stores a decimal value for the sertanejo's horizontal position
        self.x = float(self.rect.x)

        # Movement flag; starts with a static sertanejo
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Updates the sertanejo's position based on the movement flag"""
        # Updates the sertanejo's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.sertanejo_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.sertanejo_speed
        
        # Updates the rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draws the sertanejo on its current position"""
        self.screen.blit(self.image, self.rect)