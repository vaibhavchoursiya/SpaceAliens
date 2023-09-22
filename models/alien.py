import pygame

from pygame.sprite import Sprite

from models.scoreboard import ScoreBoard

class Alien(Sprite):
    """It contain Alien attributes and its Methods."""
    def __init__(self, screen, settings):
        """Initilize the aliens attributes and its methods"""
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.alien_size = (60, 50)

        # Image and Rect of image
        self.image = pygame.image.load("Images/alien.png")
        # Scale Image
        self.image = pygame.transform.scale(self.image, self.alien_size)

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 

        # x and y corrdinates.
        self.x = self.rect.x
        self.y = self.rect.y

    # Overriding update method
    # Update alien position only y -corrdiates.
    def update(self):
        """Update alien Position."""  
        # Increase Y- corrdiate of alien.  
        self.y += self.settings.alien_speed
        self.rect.y = self.y
