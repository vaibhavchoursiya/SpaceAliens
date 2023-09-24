from pygame.sprite import Sprite

import pygame

class RedAlien(Sprite):
    """It contain all the attributes and behaviour of RedAlien."""
    def __init__(self, screen, settings ):
        """Initlize RedAlien attirbuWtes and Set its Location."""
        super().__init__()

        self.screen = screen
        self.settings = settings
        self.life = 2

        # Load Image and get its Rect attribute
        self.image = pygame.image.load("Images/red_alien.png")

        # Rotate Image 180
        self.image = pygame.transform.rotate(self.image, 180)

        # Rect of Image
        self.rect = self.image.get_rect()

        # X and Y
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        """Update Red Alien Location"""
        self.y += self.settings.red_alien_speed
        self.rect.y = self.y


        