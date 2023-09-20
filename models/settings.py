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

        # Ship
        self.ship_speed = 1.5

        # Bullet
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_speed = 2.5
        self.bullet_color = "white"

        # ScoreBoard
        self.scoreboard_width = self.screen_width
        self.scoreboard_height = 50 
        self.scoreboard_color = "black"

        # Alien
        self.alien_speed = 10