import pygame

from models.label import Label

from models.stats import Stats

class ScoreBoard:
    """It contain scoreboard attributes and methods."""
    def __init__(self, screen, settings):
        """Initilize Scoreboard attirbutes."""
        self.screen = screen
        self.settings = settings
        self.extra_padding = 10
        self.stats = Stats()

        # ScoreBoard
        self.scoreboard = pygame.Rect(0 , 0, self.settings.scoreboard_width, self.settings.scoreboard_height)

        # Highscore
        self.highscore = Label(
            # This value should come from database highscore.
            label=f"High Score:20",
            screen=self.screen,
            settings=self.settings
        )
        # Location of Highscore
        self.highscore.text_image_rect.x += self.extra_padding
        self.highscore.text_image_rect.centery = self.scoreboard.centery
        
        # Level
        self.level = Label(
            # This value should come from stats.
            label=f"Level:{self.stats.level}",
            screen=self.screen,
            settings=self.settings
        )
        # Location of Level
        self.level.text_image_rect.center = self.scoreboard.center

        # Score 
        self.score = Label(
            # This value should come from database score.
            label=f"Score:{self.stats.score}",
            screen=self.screen,
            settings=self.settings
        )
        # Location of score
        self.score.text_image_rect.x += self.scoreboard.width - self.extra_padding - self.score.text_image_rect.width
        self.score.text_image_rect.centery = self.scoreboard.centery

    def draw_scoreboard(self):
        """Draw ScoreBoard in screen."""
        pygame.draw.rect(
            self.screen,
            self.settings.scoreboard_color,
            self.scoreboard
        )
        self.highscore._draw_on_scoreboard()
        self.level._draw_on_scoreboard()
        self.score._draw_on_scoreboard()
