import pygame

from models.button import Button

from models.ship import Ship

from models.scoreboard import ScoreBoard

from models.alien import Alien

from pygame.sprite import Sprite

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
        
        # Bullet
        self.bullets = pygame.sprite.Group() 

        # Score Board
        self.scoreboard = ScoreBoard(
            screen=self.screen,
            settings=self.settings
        )

        # Aliens
        self.aliens = pygame.sprite.Group()


        # Alien Fleet
        self._create_alien_fleet()


        
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

    def _draw_bullets(self):
        """Draw Bullets.""" 
        
        for bullet in self.bullets.sprites().copy():
            # Remove Bullet that cross the window
            if bullet.y < 0: 
                self.bullets.remove(bullet)

        # Draw Bullet
        for bullet in self.bullets.sprites():    
            bullet.draw_bullet()   

        print(len(self.bullets))    


    def _create_alien_fleet(self):
        """create alien fleet"""

        alien1 =  Alien(self.screen, self.settings)
        # Alien spec
        alien_width = alien1.rect.width
        alien_height = alien1.rect.height
        current_x = alien1.rect.x


        while current_x < self.screen.get_rect().width - alien_width:
            # Alien Instance
            new_alien = Alien(screen=self.screen, settings=self.settings)
            new_alien.rect.x = current_x
            new_alien.x = current_x

            # Add Alien in List : Aliens
            self.aliens.add(new_alien)

            # Next corrdinate
            current_x += 2*alien_width

        
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
        self.bullets.update()

        # Alien
        # self.aliens.update()

        # Draw
        

        # ScoreBoard
        self.scoreboard.draw_scoreboard()

        # Draw ship
        self.ship.draw_ship()

        # Bullet
        self._draw_bullets()

        print(f"alien = {len(self.aliens)}")
        self.aliens.draw(self.screen)

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







