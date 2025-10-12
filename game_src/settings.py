class Settings:
    """Class to store the game configurations for Alien Invasion"""

    def __init__(self):
        """Initializes the game configurations"""
        # Screen configurations
        self.screen_width = 900
        self.screen_height= 600
        self.bg_color = (15, 20, 60)

        # Sertanejo configurations
        self.sertanejo_speed = 5
        self.sertanejo_limit = 3

        # Waterbeads configurations
        self.bead_speed = 2.0
        self.bead_width = 7
        self.bead_height = 7
        self.bead_color = (137, 181, 242)
        self.beads_allowed = 10

        # Waterdroplets configurations
        self.droplet_speed = 2.5
        self.droplet_width = 4.5
        self.droplet_height = 4.5
        self.droplet_color = (180, 211, 245)
        self.droplets_allowed = 20

        # Balloon configurations
        self.balloon_speed = 5
        self.fleet_drop_speed = 10

        # Rate of game acceleration
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializes the configurations that change along the game"""
        self.sertanejo_speed = 1.5
        self.bead_speed = 2.5
        self.balloon_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increments the speed elements"""
        self.sertanejo_speed *= self.speedup_scale
        self.bead_speed *= self.speedup_scale
        self.balloon_speed *= self.speedup_scale
