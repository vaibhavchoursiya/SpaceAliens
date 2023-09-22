from pygame.sprite import Sprite

import pygame

from random import choice

class Bullet(Sprite):
    """It contain bullet attributes and methods."""
    def __init__(self, screen, settings, ship, id):
        """Initilize bullet and set its Initial Location."""
        super().__init__()

        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullet_id = id

        # Create Bullet
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        # Location
        self.rect.midbottom = self.ship.rect.midtop

        # y corrdinates
        self.y = self.rect.y

    # update bullet location
    def update(self):
        """Update Location of bullet."""
        # it only update those bullets that have id divide by 6
        # It give a illusion of gap between bullets.
        if self.bullet_id % self.settings.bullet_visible == 0 :
            self.y -= self.settings.bullet_speed
            self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw Bullet on screen."""
        selected_color = choice(self.settings.color)
        pygame.draw.rect(self.screen,
                        selected_color,
                        self.rect)
        