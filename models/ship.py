
import pygame

class Ship:
    """It contain ship attributes and methods."""
    def __init__(self, screen, settings):
        """Initialize the ship and set its Location."""
        self.screen = screen
        self.settings = settings

        # Rect object of screen
        self.screen_rect = screen.get_rect()

        # Load Image and get Its rect attributes
        self.image = pygame.image.load("Images/ship.png")
        self.rect = self.image.get_rect()

        # Ship at Mid Bottom of Screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # x corrdinates
        self.x = self.rect.x

        # Moving Flags
        self.right = False
        self.left = False

    # Update ship position
    def update(self):
        """Update left or right corrdinates of ship."""
        if self.right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        elif self.left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x   


    # Draw Ship
    def draw_ship(self):
        """Draw ship on screen."""
        self.screen.blit(self.image, self.rect)
