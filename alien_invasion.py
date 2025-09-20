import sys
import pygame

class AlienInvasion:
    """General class to manage actions and behaviors within the game"""
    
    def __init__(self):
        """Initializes the game and creates resources for it"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Initiates the game's main loop"""
        while True:
            # Observes keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Leaves visible the most recently drawn screen
            pygame.display.flip()

if __name__ == '__main__':
    # Instantiates and executes the game
    ai = AlienInvasion()
    ai.run_game()