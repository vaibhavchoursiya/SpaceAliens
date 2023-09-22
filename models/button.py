import pygame.font

class Button:
    """It contain button attributes and methods"""
    def __init__(self, screen, settings, msg, background_color):
        """Initilize button and set its initial location."""
        self.screen = screen
        self.settings = settings
        self.font_size = 24
        self.extra_padding = 10
        self.background_color = background_color

        # Text font
        self.font = pygame.font.Font("Images/PressStart2P.ttf",self.font_size)

        # Create Text Image
        self._pre_text(msg=msg)

        # Button rect object
        self.rect = pygame.Rect(0, 0, self.text_image_rect.width + self.extra_padding, self.text_image_rect.height + self.extra_padding)


# Helper Method
    def _pre_text(self, msg):
        """Text to Text Image."""       
        # Rendering the Font.
        self.text_image = self.font.render(
            msg,
            True,
            "black",
            self.background_color
            )
        
        # Image Rect object
        self.text_image_rect = self.text_image.get_rect()

# -------------------------------------------------------------------

# Draw Text and Button
    def draw_button(self,y=None):
        """Draw Button of screen."""
        # Setting Location
        self.rect.centerx = self.screen.get_rect().centerx
        if y == None:
            self.rect.centery = self.screen.get_rect().centery
            
        else:    
            self.rect.centery = y    

        # Set Text Image center corrdinates.
        self.text_image_rect.centery = self.rect.centery
        self.text_image_rect.centerx = self.rect.centerx
        
        # Draw Rect
        pygame.draw.rect(self.screen, self.background_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)