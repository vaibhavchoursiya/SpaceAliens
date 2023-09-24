import pygame

from models.button import Button

from models.ship import Ship

from models.scoreboard import ScoreBoard

from models.alien import Alien

from models.stats import Stats

from models.bullets import Bullet

from time import sleep

from database.game_database import *

from models.label import Label

from random import randint

from models.red_alien import RedAlien



class Screens:
    """It contain different screens."""
    def __init__(self,screen,settings):
        """Initilize screens."""
        self.screen = screen
        self.settings = settings

        # Load Image
        self.image = pygame.image.load("Images/background.jpg")
        self.image1 = pygame.image.load("Images/background1.jpg")


        # Bullet id
        self.bullet_id = 0

        # Stats instance
        self.stats = Stats()

        self._set_screen(s1=True)

        # Buttons
        self._intro_screen_button()
        self._gameover_screen_button()
        
        
        



        
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
            msg=f"Level:{self.stats.level}",
            screen=self.screen,
            settings=self.settings)


# GameOver screen button
    def _gameover_screen_button(self):
        """Intro screen buttons."""
        self.gameover = Button(
            background_color="white",
            msg="Game Over",
            screen=self.screen,
            settings=self.settings)

        self.back_intro = Button(
            background_color="white",
            msg="< Back",
            screen=self.screen,
            settings=self.settings)

    # Set Screen
    def _set_screen(self,s1=False, s2=False, s3=False, s4=False, s5=False, s6=False):
        """Set screen which value is True."""    
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

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

        alien1 =  Alien(self.screen, self.settings,0)
        # Alien spec
        alien_width = alien1.rect.width
        alien_height = alien1.rect.height
        current_x = alien1.rect.x
        current_y = alien1.rect.y

        # # Column
        # It Create NEXT Row Every Time it runs

        # alien id 
        alien_id = 0

        while current_y < self.stats.level*2*alien_height:

            # Row
            while current_x < self.screen.get_rect().width - alien_width:
                # Alien Instance
                new_alien = Alien(screen=self.screen, settings=self.settings, id=alien_id)
                
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

                # Alien Id
                alien_id += 1

            # # Reset x
            current_x = alien_width

            # # Next corrdinate
            current_y += 2*alien_height

        rand_id = randint(1, alien_id)
        for alien in self.aliens.sprites().copy():
            if alien.id == rand_id:
                x = alien.x
                y = alien.y
                id = alien.id
                
                red_alien = RedAlien(
                    settings=self.settings,
                    screen=self.screen,
                    id = id
                )
                # x
                red_alien.rect.x = x
                red_alien.x= x

                # y
                red_alien.rect.y = y
                red_alien.y = y

                # Remove alien
                self.aliens.remove(alien)

                self.red_aliens.add(red_alien)    
                



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
            # Update Highscore
            highscore = read_data()
            # Update the highscore if current score is greater than
            # Saved highscore.
            if  self.stats.score > int(highscore):
                write_data(self.stats.score)
            self._set_screen(s3=True)
            print("collide ship and alien")


    # Check All aliens are distroied
    def _check_all_aliens_are_distroied(self):
        """"Check All aliens are distroied."""
        # If aliens are empty.
        if not self.aliens:
            # Pre Next Level Screen
            self.aliens.empty()
            self.red_aliens.empty()
            self._set_screen(s6=True)
           


# -----------------------------------


    # Intro Screen
    def intro_screen(self):
        """intro screen."""
        self.screen.blit(self.image,(0, 0))
        # Reset Settings
        self.settings.reset_settings()

        # Intro Label
        self.intro_label1 = Label(
            label="Space",
            font_size=80,
            screen=self.screen,
            settings=self.settings
        )
        self.intro_label1.draw_on_intro_screen(
            x=-20
        )

        self.intro_label2 = Label(
            label="Aliens",
            font_size=60,
            screen=self.screen,
            settings=self.settings,
        )
        self.intro_label2.draw_on_intro_screen(
            x=120,
            y=166
        )

        # Button
        self.play.draw_button(self.settings.screen_height/2 + 20)
        self.level.draw_button(self.settings.screen_height/2 + 70)

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
        self.red_aliens = pygame.sprite.Group()


        # Alien Fleet
        self._create_alien_fleet()


        self._update_screen()


    # Pre Main Screen
    def pre_main_screen(self):
        """Screen Before Main Screen"""
        self.screen.blit(self.image1, (0, 0))
        i = 3
        while i > 0:
                
            # Label or Button
            self.countdown = Button(
            background_color="white",
            msg=f"{i}",
            screen=self.screen,
            settings=self.settings)

           

            # Draw ScoreBoard
            self.scoreboard.draw_scoreboard()

            # Draw Alien
            self.aliens.draw(self.screen)
            self.red_aliens.draw(self.screen)

            # Draw Ship
            self.ship.draw_ship()

            # Draw Button
            self.countdown.draw_button()

            self._update_screen()

            # Label
            sleep(1)
            i-=1

        self._set_screen(s2=True)






    # Main Screen
    def main_screen(self):
        """Main Screen."""   
        self.screen.blit(self.image1, (0, 0))

        
    # Create Bullets
        self._create_bullets()

    # Update

        # Ship
        self.ship.update() 

        # Bullets
        self.bullets.update()

        # Alien
        self.aliens.update()
        self.red_aliens.update()

    # Collide between alien and Bullet
        self._collide_between_aliens_and_bullets()

        # Update score board
        self.scoreboard.update()

  

    # Draw
        

        # ScoreBoard
        self.scoreboard.draw_scoreboard()

        # Draw ship
        self.ship.draw_ship()

        
        # Bullet
        self._draw_bullets()

        # Alien 
        self.aliens.draw(self.screen)
        self.red_aliens.draw(self.screen)

        self._update_screen()


    # Collide between alien and ship or alien cross the ship
        self._collide_alien_and_ship()    

    # Check if every alien is distroed or not.
    # if they then go to next level.
        self._check_all_aliens_are_distroied()  


    # Game over
    def game_over(self):
        """Game Over."""   
        self.screen.blit(self.image1, (0, 0))

        self.gameover.draw_button(self.settings.screen_height/2 - 17)
        self.back_intro.draw_button(self.settings.screen_height/2 + 40)

        
        self._update_screen()

        # Reset Things
        self.stats._reset_stats()


    # Pre Next Level Screen
    def pre_next_level(self):
        """Screen before next_level."""
        self.screen.blit(self.image1, (0, 0))


        i = 3
        while i > 0:
            # Label or Button
            self.countdown = Button(
            background_color="white",
            msg=f"{i}",
            screen=self.screen,
            settings=self.settings)

            self.next_level_label = Button(
            background_color="white",
            msg=f"Next Level {self.stats.level} in",
            screen=self.screen,
            settings=self.settings)

            # Draw
            self.countdown.draw_button()
            self.next_level_label.draw_button(y=self.settings.screen_height/2 - 50)

            self._update_screen()

            sleep(1)
            
            i -= 1

        
        # Updates :- Level, Ship Speed, Alien Speed, Bullet Speed
        # Update Level
        self.stats.update_level()
        self.settings.update(self.stats.level)

        
         
        
        # Bullets
        self.bullets.empty()

        # Create Alien Fleet
        # Modified This Method for create one extra alien.
        self._create_alien_fleet()

        self.ship.initial_position_of_ship()

        # Next Level Screen.
        self._set_screen(s4=True)



    # Next Level
    def next_level(self):
        """Next Level."""    
        print(f"alien_speed:{self.settings.alien_speed}")
        self.main_screen()
