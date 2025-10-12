import sys
import pygame
from time import sleep
from random import randint
from settings import Settings
from gamestats import GameStats
from sertanejo import Sertanejo
from beads import Bead
from balloon import Balloon
from button import Button

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

        # Creates an instance to store game statistics
        self.stats = GameStats(self)
        
        self.sertanejo = Sertanejo(self)
        self.beads = pygame.sprite.Group()
        self.balloons = pygame.sprite.Group()

        self._create_fleet()

        self.clock = pygame.time.Clock()

        # Initalizes the background music
        # pygame.mixer.music.load('sounds/background_music.mp3')
        # pygame.mixer.music.play(-1)  # Loops the music indefinitely

        # Initializes sound effects
        # self.bead_sound = pygame.mixer.Sound('sounds/bead_shoot.wav')

        # Initializes the game over sound
        # self.game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')

        # Sets the volume for music and sound effects
        # pygame.mixer.music.set_volume(0.5)
        # self.bead_sound.set_volume(0.7)
        # self.game_over_sound.set_volume(0.7)

        # Initializes Eric Marshes in an active state
        self.game_active = False

        # Creates the Play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Initiates the game's main loop"""
        while True:
            self._check_events()

            if self.game_active:
                self.sertanejo.update()
                self._update_beads()
                self._update_balloons()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def  _check_play_button(self, mouse_pos):
        """Starts a new game when the player clicks Play"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True

    def _check_keydown_events(self, event):
        """Responds to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.sertanejo.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.sertanejo.moving_left = True
        elif event.key == pygame.K_ESCAPE:
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
        if len(self.beads) < self.settings.beads_allowed:
            new_bead = Bead(self)
            self.beads.add(new_bead)
    
    def _update_beads(self):
        """Removes beads that have disappeared"""
        # Updates the position of the beads
        self.beads.update()

        # Removes beads that have gone off the top of the screen
        for bead in self.beads.copy():
            if bead.rect.bottom <= 0:
                self.beads.remove(bead)
        
        self._check_bead_balloon_collisions()
    
    def _check_bead_balloon_collisions(self):
        """Responds to bead-balloon collisions"""
        collisions = pygame.sprite.groupcollide(
            self.beads, self.balloons, True, True)
        
        if not self.balloons:
            # Destroys existing beads and creates a new fleet
            self.beads.empty()
            self._create_fleet()
    
    def _sertanejo_hit(self):
        """Responds to the sertanejo being hit by a balloon"""
        if self.stats.sertanejo_left > 0:
            # Decrements sertanejo_left
            self.stats.sertanejo_left -= 1

            # Empties the list of balloons and beads
            self.balloons.empty()
            self.beads.empty()

            # Creates a new fleet and centers the sertanejo
            self._create_fleet()
            self.sertanejo.center_sertanejo()

            # Pauses
            sleep(0.5)
        else:
            self.game_active = False
            # Plays the game over sound
            # self.game_over_sound.play()
            pygame.mouse.set_visible(True)

    def _check_balloons_bottom(self):
        """Checks if any balloons have reached the bottom of the screen"""
        for balloon in self.balloons.sprites():
            if balloon.rect.bottom >= self.settings.screen_height:
                # Treats this the same as if the sertanejo got hit
                self._sertanejo_hit()
                break

    def _update_balloons(self):
        """Checks if the fleet reached an edge, then updates the positions 
        of all balloons in the fleet"""
        self._check_fleet_edges()
        self.balloons.update()

        # Looks for balloon-sertanejo collisions
        if pygame.sprite.spritecollideany(self.sertanejo, self.balloons):
            self._sertanejo_hit()

        # Looks for balloons that have reached the bottom of the screen
        self._check_balloons_bottom()

    def _create_fleet(self):
        """Creates a fleet of balloons"""
        # Creates a balloon
        balloon = Balloon(self)
        balloon_width, balloon_height = balloon.rect.size
        
        current_x, current_y = balloon_width, balloon_height
        while current_y < (self.settings.screen_height - 11 * balloon_height):
            while current_x < (self.settings.screen_width - 2 * balloon_width):
                self._create_balloon(current_x, current_y)
                random_number = randint(2, 19)
                current_x += random_number * balloon_width
            
            # Ends a row; redefines the x value, and increments the y value
            current_x = balloon_width
            current_y += 5 * balloon_height

    def _create_balloon(self, x_position, y_position):
        """Creates a balloon and places it in the current row"""
        new_balloon = Balloon(self)
        new_balloon.rect.x = x_position
        new_balloon.x = x_position
        new_balloon.rect.y = y_position
        self.balloons.add(new_balloon)

    def _check_fleet_edges(self):
        """Responds appropriately if any balloons have reached an edge"""
        for balloon in self.balloons.sprites():
            if balloon.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drops the entire fleet and changes its direction"""
        for balloon in self.balloons.sprites():
            balloon.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Redraws the screen with each loop"""
        self.screen.fill(self.settings.bg_color)
        for bead in self.beads.sprites():
            bead.draw_bead()
        self.sertanejo.blitme()
        self.balloons.draw(self.screen)

        # Draws the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()

        # Leaves visible the most recently drawn screen
        pygame.display.flip()

if __name__ == '__main__':
    # Instantiates and executes the game
    em = EricMarshes()
    em.run_game()