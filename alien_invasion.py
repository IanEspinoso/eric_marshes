import sys
import pygame
from settings import Settings

class AlienInvasion:
    """General class to manage actions and behaviors within the game"""
    
    def __init__(self):
        """Initializes the game and creates resources for it"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Initiates the game's main loop"""
        while True:
            # Observes keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraws the screen with each loop
            self.screen.fill(self.settings.bg_color)

            # Leaves visible the most recently drawn screen
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Instantiates and executes the game
    ai = AlienInvasion()
    ai.run_game()