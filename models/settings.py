class Settings:
    """It contain all the settings require in game."""
    def __init__(self):
        """Initilize game settings."""
        # Width and Height
        self.screen_width = 700
        self.screen_height = 690

        # Background color
        self.bg_color = "grey"

        # Frame rate
        self.frame_rate = 60


        # Bullet
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = "white"
        # Make Bullet visible.
        # only those bullets that can whole divide by this number.
        self.bullet_visible = 7

        # ScoreBoard
        self.scoreboard_width = self.screen_width
        self.scoreboard_height = 50 
        self.scoreboard_color = "black"
        
        # Level List
        self.LEVEL_LIST = []

        self._create_level()

# Helper Method
    def _create_level(self):
        """Create Levels"""
        for i in range(2, 10):
            dic = {}
            
            # Create Level
            dic["alien_speed"] = 0.3 + (i/10)
            dic["red_alien_speed"] = 0.6 + (i/10)
            dic["ship_speed"] = 2.0 + (i/10)
            dic["bullet_speed"] = 2.0 + (i/10)
            dic["red_alien_bullet_speed"] = 1.0 + (i/10)
           
            self.LEVEL_LIST.append(dic)
# ---------------------------------------------------------


    # Reset Settings   
    def reset_settings(self):
        """Reset the settings:"""
        # Bullet
        self.bullet_speed = 2.0
        self.red_alien_bullet_speed = 1.0

        # Alien
        self.alien_speed = 0.3
        self.red_alien_speed = 0.6

        # Ship
        self.ship_speed = 2.0

        # Color
        self.color = ["red", "green", "white", "yellow", "blue", "pink", "orange"]


    # Update Settings
    def update(self, level):
        """Update settings : ship_speed, bullet_speed and alien_speed """    
        
        # Bullet
        self.bullet_speed  = self.LEVEL_LIST[level]["bullet_speed"]
        self.red_alien_bullet_speedspeed  = self.LEVEL_LIST[level]["red_alien_bullet_speed"]


        # Alien
        self.alien_speed = self.LEVEL_LIST[level]["alien_speed"]
        self.red_alien_speed = self.LEVEL_LIST[level]["red_alien_speed"]


        # Ship
        self.ship_speed = self.LEVEL_LIST[level]["ship_speed"]
        