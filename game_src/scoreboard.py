import pygame.font
from pygame.sprite import Group
from sertanejo import Sertanejo

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, em_game):
        """Initializes the scoring attributes"""
        self.em_game = em_game
        self.screen = em_game.screen
        self.screen_rect= self.screen.get_rect()
        self.settings = em_game.settings
        self.stats = em_game.stats

        # Font settings for score information
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prepares the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_sertanejos()

    def check_high_score(self):
        """ Verifies if there is a new max score """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_score(self):
        """Turns the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)
        
        # Displays the score on the top right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_level(self):
        """ Transforms the level into a rendered image """
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color)
        
        # Places the level below the points
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_sertanejos(self):
        """Displays the remaining sertanejos"""
        self.sertanejos = Group()
        for sertanejo_number in range(self.stats.sertanejos_left):
            sertanejo = Sertanejo(self.em_game)
            sertanejo.rect.x = 10 + sertanejo_number * sertanejo.rect.width
            sertanejo.rect.y = 10
            self.sertanejos.add(sertanejo)

    def prep_high_score(self):
        """ Transforms the scoring into a rendered image """
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)
        
        # Centers the max score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draws the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.sertanejos.draw(self.screen)