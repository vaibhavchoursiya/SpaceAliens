import pygame

class Sheild:
    """It contain all the attributes and behaviours of Sheild."""
    def __init__(self, screen, settings, ship):
        """Initilize Sheild attirbute and set its Initial Location."""
        self.screen= screen
        self.settings = settings
        self.ship = ship

        # Sheild Rect object
        self.rect = pygame.Rect(0, 0, self.settings.sheild_width, self.settings.sheild_height)

        # Location
        self.rect.midbottom = self.ship.rect.midtop

        # Flag
        self.draw = False

    def update(self):
        """Update location of Sheild."""    
        self.rect.midbottom = self.ship.rect.midtop

    def draw_sheild(self):
        """Draw Sheild Front of Ship."""

        if self.draw:
            print("draw sheild")
            pygame.draw.rect(self.screen, "white", self.rect)
