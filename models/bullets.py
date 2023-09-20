from pygame.sprite import Sprite

import pygame

class Bullet(Sprite):
    """It contain bullet attributes and methods."""
    def __init__(self, screen, settings, ship):
        """Initilize bullet and set its Initial Location."""
        super().__init__()

        self.screen = screen
        self.settings = settings
        self.ship = ship

        # Create Bullet
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        # Location
        self.rect.midbottom = self.ship.rect.midtop

        # y corrdinates
        self.y = self.rect.y

    # update bullet location
    def update(self):
        """Update Location of bullet."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw Bullet on screen."""
        pygame.draw.rect(self.screen,
                        self.settings.bullet_color,
                        self.rect)
        