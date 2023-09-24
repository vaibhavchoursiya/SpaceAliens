import pygame

from pygame.sprite import Sprite

from models.scoreboard import ScoreBoard

class Alien(Sprite):
    """It contain Alien attributes and its Methods."""
    def __init__(self, screen, settings, id):
        """Initilize the aliens attributes and its methods"""
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.alien_size = (60, 50)
        self.id = id

        # Image and Rect of image
        self.image = pygame.image.load("Images/green_alien.png")

        # Rotate Alien 180
        self.image = pygame.transform.rotate(self.image, 180)
        
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
