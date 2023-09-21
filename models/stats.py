from models.settings import Settings

class Stats:
    """It contain stats attributes."""
    def __init__(self):
        """Initilize stats attributes."""
        self.settings = Settings()
        self.level = 1
        self.score = 0


# Helper Method
    def _reset_stats(self):
        """Reset Stats."""    
        self.level = 1
        self.score = 0

# Update level:
    def update_level(self):
        """Update Level of game."""
        self.level += 1
        
        # Update settings

# Update score 
    def update_score(self):
        """Update score when alien hit."""
        self.score += 1