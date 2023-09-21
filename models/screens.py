import pygame

from models.button import Button

from models.ship import Ship

from models.scoreboard import ScoreBoard

from models.alien import Alien

from models.stats import Stats

from models.bullets import Bullet

class Screens:
    """It contain different screens."""
    def __init__(self,screen,settings):
        """Initilize screens."""
        self.screen = screen
        self.settings = settings

        # Bullet id
        self.bullet_id = 0

        # Stats instance
        self.stats = Stats()

        self._set_screen(s1=True)

        self._intro_screen_button()
        
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
            settings=self.settings,
            stats= self.stats
            
        )

        # Aliens
        self.aliens = pygame.sprite.Group()


        # Alien Fleet
        self._create_alien_fleet()



        
# Helper Methods.

    # Intro screen button
    def _intro_screen_button(self):
        """Intro screen buttons."""
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

    # Draw Bullets
    def _draw_bullets(self):
        """Draw Bullets.""" 
        
        for bullet in self.bullets.sprites().copy():
            # Remove Bullet that cross the window
            if bullet.y < 0 or bullet.bullet_id % self.settings.bullet_visible != 0: 
                self.bullets.remove(bullet)

        # Draw Bullet
        for bullet in self.bullets.sprites():    
            bullet.draw_bullet()   

        print(len(self.bullets))    

    # Create Alien Fleet
    def _create_alien_fleet(self):
        """create alien fleet"""

        alien1 =  Alien(self.screen, self.settings)
        # Alien spec
        alien_width = alien1.rect.width
        alien_height = alien1.rect.height
        current_x = alien1.rect.x
        current_y = alien1.rect.y

        # # Column
        while current_y < self.screen.get_rect().height - 2*alien_height:

            # Row
            while current_x < self.screen.get_rect().width - alien_width:
                # Alien Instance
                new_alien = Alien(screen=self.screen, settings=self.settings)
                
                # X
                new_alien.rect.x = current_x
                new_alien.x = current_x
                
                # Y
                new_alien.rect.y = current_y
                new_alien.y = current_y

                # Add Alien in List : Aliens
                self.aliens.add(new_alien)

                # Next corrdinate
                current_x += 2*alien_width

            # # Reset x
            current_x = alien_width

            # # Next corrdinate
            current_y += 2*alien_height


    # Collide Between aliens and bullets 
    def _collide_between_aliens_and_bullets(self):
        """Check Collide Between Aliens and Bullets ,
        Delete Both of them.
        """        
        if pygame.sprite.groupcollide(self.aliens, self.bullets, True, True):
            # Increase score of Player.
            self.stats.update_score()

    # Create Bullets
    def _create_bullets(self):
        """Create Bullet object and in bullets List."""
        new_bullet = Bullet(
            screen=self.screen,
            settings= self.settings,
            ship=self.ship,
            id = self.bullet_id
        )        
        self.bullet_id+=1
        self.bullets.add(new_bullet)


    # Check Alien crossed ship
    def _alien_crossed_ship(self):
        for alien in self.aliens.sprites():
            # If alien reached the bottom of screen without hitting bullet.
            if alien.rect.y > self.screen.get_rect().height - alien.rect.height:
                print("alien crossed the widn")
                return True


    # Check ship and alien collided
    def _collide_alien_and_ship(self):
        """ If alien and ship collided switch to game over screen"""
        if pygame.sprite.spritecollideany(self.ship, self.aliens) or self._alien_crossed_ship():
            self._set_screen(s3=True)
            print("collide ship and alien")

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
        self.screen.fill("red")
        
    # Create Bullets
        self._create_bullets()

    # Update

        # Ship
        self.ship.update() 

        # Bullets
        self.bullets.update()

        # Alien
        self.aliens.update()

    # Collide between alien and Bullet
        self._collide_between_aliens_and_bullets()

        # Update score board
        self.scoreboard.update()


    # Collide between alien and ship or alien cross the ship
        self._collide_alien_and_ship()    

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


        # self.screen.fill("pink")
        self._update_screen()


    # Next Level
    def next_level(self):
        """Next Level."""    
        self.screen.fill("orange")
        self._update_screen()







