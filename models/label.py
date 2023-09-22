import pygame.font

from random import choice

class Label:
    """It contain label attirbutes and methods."""
    def __init__(self, label, screen, settings, font_size=10):
        """Initilize Label attributes and set it Initial Location."""
        self.screen = screen
        self.settings = settings
        self.font_size = font_size
        self.label = label
        

        # Font
        self.font = pygame.font.Font("Images/PressStart2P.ttf", self.font_size)

        # Font to Image
        self._pre_text()


# Helper Method
    def _pre_text(self):
        """Text to Image."""
        self.text_image = self.font.render(
            self.label,
            True,
            "white",
            "black"
        )

        # Rect
        self.text_image_rect = self.text_image.get_rect()

    def _draw_on_scoreboard(self):
        """Draw on Scoreboard."""
        
        # Draw Image.
        self.screen.blit(self.text_image, self.text_image_rect)


    def draw_on_intro_screen(self, x=0, y=100):
        """Draw on intro screen."""    
        # Select Color
        selected = choice(self.settings.color)

        # Render font
        self.text_image = self.font.render(
            self.label,
            True,
            selected,
            "black"
        )    

        # Set text_image x and y corrdinates.
        self.text_image_rect.centerx = x + self.screen.get_rect().centerx
        self.text_image_rect.centery = y

        # Draw Image.
        self.screen.blit(self.text_image, self.text_image_rect)