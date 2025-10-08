import sys
import pygame
from settings import Settings
from sertanejo import Sertanejo
from beads import Bead

class EricMarshes:
    """General class to manage actions and behaviors within the game"""
    
    def __init__(self):
        """Initializes the game and creates resources for it"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Eric Marshes")

        self.sertanejo = Sertanejo(self)
        self.beads = pygame.sprite.Group()

        self.clock = pygame.time.Clock()
    

    def run_game(self):
        """Initiates the game's main loop"""
        while True:
            self._check_events()
            self.sertanejo.update()
            self.beads.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Responds to keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    
    def _check_keydown_events(self, event):
        """Responds to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.sertanejo.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.sertanejo.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._shoot_bead()
    
    def _check_keyup_events(self, event):
        """Responds to key releases"""
        if event.key == pygame.K_RIGHT:
            self.sertanejo.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.sertanejo.moving_left = False
    
    def _shoot_bead(self):
        """Creates a new bead and adds it to the beads group"""
        new_bead = Bead(self)
        self.beads.add(new_bead)

    def _update_screen(self):
        """Redraws the screen with each loop"""
        self.screen.fill(self.settings.bg_color)
        for bead in self.beads.sprites():
            bead.draw_bead()
        self.sertanejo.blitme()

        # Leaves visible the most recently drawn screen
        pygame.display.flip()

if __name__ == '__main__':
    # Instantiates and executes the game
    em = EricMarshes()
    em.run_game()