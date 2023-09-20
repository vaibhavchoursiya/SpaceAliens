import pygame

from models.button import Button

from models.ship import Ship

class Screens:
    """It contain different screens."""
    def __init__(self,screen,settings):
        """Initilize screens."""
        self.screen = screen
        self.settings = settings

        self._set_screen(s1=True)

        self.play = Button(
            background_color="white",
            msg="New Game",
            screen=self.screen,
            settings=self.settings)

        self.level = Button(
            background_color="white",
            msg="Level",
            screen=self.screen,
            settings=self.settings)
        
        # Ship
        self.ship = Ship(
            screen=self.screen,
            settings=self.settings
            )
        
# Helper Methods.
    # Set Screen
    def _set_screen(self,s1=False, s2=False, s3=False, s4=False):
        """Set screen which value is True."""    
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    # Update screen
    def _update_screen(self):
        """Update Screen."""    
        # Make Recently drawn screen visible.
        pygame.display.flip()
# -----------------------------------


    # Intro Screen
    def intro_screen(self):
        """intro screen."""
        # Button
        self.play.draw_button(self.settings.screen_height/2 - 10)
        self.level.draw_button(self.settings.screen_height/2 + 40)


        self._update_screen()

    # Main Screen
    def main_screen(self):
        """Main Screen."""   
        self.screen.fill("black")

        # Ship
        self.ship.update() 

        # Draw Ship
        self.ship.draw_ship()

        self._update_screen()


    # Game over
    def game_over(self):
        """Game Over."""    
        self.screen.fill("pink")
        self._update_screen()


    # Next Level
    def next_level(self):
        """Next Level."""    
        self.screen.fill("orange")
        self._update_screen()







