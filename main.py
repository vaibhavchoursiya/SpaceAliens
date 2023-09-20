import pygame

from helper import Helper

from models.settings import Settings


class SpaceAliens:
    """It contain Game Resources and methods."""
    def __init__(self):
        """Initilize game and its resources."""     
        # Initilize Background settings for Pygame.
        pygame.init()

        
        # Settings
        self.settings = Settings()

        # Surface object of screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Caption
        pygame.display.set_caption("SpaceAliens")

        # Clock
        self.clock = pygame.time.Clock()

        # Helper Instance
        self.hp = Helper(screen=self.screen,settings = self.settings)

    
    def run_game(self):
        """Run the game."""
        # Game Loop
        while True:
            self.hp.check_event()

            if self.hp.screens.s1:
                self.hp.screens.intro_screen()

            elif self.hp.screens.s2:
                self.hp.screens.main_screen()

            elif self.hp.screens.s3:
                self.hp.screens.game_over()    

            if self.hp.screens.s4:
                self.hp.screens.next_level()    


            self.clock.tick(self.hp.settings.frame_rate)


if __name__ == "__main__":
    # Instance of SpcaceAliens.
    sa = SpaceAliens()
    sa.run_game()