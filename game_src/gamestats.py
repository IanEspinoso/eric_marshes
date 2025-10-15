class GameStats:
    """Tracks statistics for Eric in the Marshes."""

    def __init__(self, em_game):
        """Initializes statistics."""
        self.settings = em_game.settings
        self.reset_stats()
        # Max score shouldn't be rewritten
        self.high_score = 0

    def reset_stats(self):
        """Initializes statistics that can change during the game."""
        self.sertanejo_left = self.settings.sertanejo_limit
        self.score = 0
        self.level = 1