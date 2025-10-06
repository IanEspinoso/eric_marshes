class Settings:
    """Class to store the game configurations for Alien Invasion"""

    def __init__(self):
        """Initializes the game configurations"""
        # Screen configurations
        self.screen_width = 900
        self.screen_height= 600
        self.bg_color = (15, 20, 60)

        # Sertanejo configurations
        self.sertanejo_speed = 10

        # Waterbeads configurations
        self.bead_speed = 2.0
        self.bead_width = 4.5
        self.bead_height = 4.5
        self.bead_color = (137, 181, 242)

        # Waterdroplets configurations
        self.droplet_speed = 2.5
        self.droplet_width = 3
        self.droplet_height = 3
        self.droplet_color = (180, 211, 245)
