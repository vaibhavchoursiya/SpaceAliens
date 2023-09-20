class Settings:
    """It contain all the settings require in game."""
    def __init__(self):
        """Initilize game settings."""
        # Width and Height
        self.screen_width = 700
        self.screen_height = 500

        # Background color
        self.bg_color = "grey"

        # Frame rate
        self.frame_rate = 60