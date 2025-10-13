import pygame.font

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, em_game):
        """Initializes the scoring attributes"""

        self.screen = em_game.screen
        self.screen_rect= self.screen.get_rect()
        self.settings = em_game.settings
        self.stats = em_game.stats

        # Font settings for score information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepares the initial score image
        self.prep_score()
    
    def prep_score(self):
        """Turns the score into a renderized image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)
        
        # Displays the score on the top right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self..screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draws the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)