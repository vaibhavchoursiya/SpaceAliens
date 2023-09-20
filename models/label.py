import pygame.font

class Label:
    """It contain label attirbutes and methods."""
    def __init__(self, label, screen, settings):
        """Initilize Label attributes and set it Initial Location."""
        self.screen = screen
        self.settings = settings
        self.font_size = 15
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