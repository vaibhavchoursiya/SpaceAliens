import pygame

from pygame.sprite import Sprite

class AlienBullet(Sprite):
    """It contain all the attributes and behaviour of Alien Bullet."""
    def __init__(self, screen, settings, alien_ship,id):
        super().__init__()

        self.screen = screen
        self.settings = settings
        self.alien_ship = alien_ship
        self.id = id

        # Bullet Rect object
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        # Location
        self.rect.midtop = self.alien_ship.rect.midbottom

        # Y
        self.y = self.rect.y

    def update(self):
        """Update Alien Bullet."""
        if self.id % 12 == 0:
            self.y += self.settings.red_alien_bullet_speed
            self.rect.y = self.y

    def draw_alien_bullet(self):
        """Draw Alien Bullet."""
        color = "red"

        # Draw Bullet
        pygame.draw.rect(self.screen,color,self.rect)