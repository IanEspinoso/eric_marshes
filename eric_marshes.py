import sys
import pygame
from settings import Settings
from sertanejo import Sertanejo

class EricMarshes:
    """General class to manage actions and behaviors within the game"""
    
    def __init__(self):
        """Initializes the game and creates resources for it"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Eric Marshes")

        self.sertanejo = Sertanejo(self)
    

    def run_game(self):
        """Initiates the game's main loop"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Responds to keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Moves the hero to the right
                    self.sertanejo.rect.x += 1
    
    def _update_screen(self):
        """Redraws the screen with each loop"""
        self.screen.fill(self.settings.bg_color)
        self.sertanejo.blitme()

        # Leaves visible the most recently drawn screen
        pygame.display.flip()

if __name__ == '__main__':
    # Instantiates and executes the game
    em = EricMarshes()
    em.run_game()