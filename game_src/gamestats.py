class GameStats:
    """Tracks statistics for Eric in the Marshes."""

    def __init__(self, em_game):
        """Initializes statistics."""
        self.settings = em_game.settings
        self.reset_stats()
        # Max score should be retrieved from records
        filename = "../misc/high_score.txt"
        try:
            with open(filename, 'r') as file:
                high_score = file.readline().strip()
                print(f"High score is {int(high_score)}")
                self.high_score = int(high_score)
        except FileNotFoundError:
            print("Previous high score not found.")
            self.high_score = 0

    def reset_stats(self):
        """Initializes statistics that can change during the game."""
        self.sertanejos_left = self.settings.sertanejo_limit
        self.level = 1
        self.score = 0