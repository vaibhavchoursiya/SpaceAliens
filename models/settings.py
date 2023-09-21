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
        self.ship_speed = 2.5

        # Bullet
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_speed = 3.0
        self.bullet_color = "white"
        # Make Bullet visible.
        # only those bullets that can whole divide by this number.
        self.bullet_visible = 7

        # ScoreBoard
        self.scoreboard_width = self.screen_width
        self.scoreboard_height = 50 
        self.scoreboard_color = "black"

        # Alien
        self.alien_speed = 0.2