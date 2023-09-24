from pygame.sprite import Sprite

import pygame

class RedAlien(Sprite):
    """It contain all the attributes and behaviour of RedAlien."""
    def __init__(self, screen, settings, id ):
        """Initlize RedAlien attirbuWtes and Set its Location."""
        super().__init__()

        self.screen = screen
        self.settings = settings
        self.id = id
        self.life = 2
        self.alien_size = (60, 50)

        # Load Image and get its Rect attribute
        self.image = pygame.image.load("Images/red_alien.png")

        # Rotate Image 180
        self.image = pygame.transform.rotate(self.image, 180)

        # Scale Image
        self.image = pygame.transform.scale(self.image, self.alien_size)

        # Rect of Image
        self.rect = self.image.get_rect()

        # X and Y
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        """Update Red Alien Location"""
        self.y += self.settings.red_alien_speed
        self.rect.y = self.y


        