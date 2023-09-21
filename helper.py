
import pygame

import sys

from models.screens import Screens

from models.bullets import Bullet

class Helper:
    """It contain helper methods"""
    def __init__(self, screen, settings):
        """Initlize the helper class."""

        # Surface object of screen/window
        self.screen = screen

        # Settings
        self.settings = settings 

        # Screens
        self.screens = Screens(screen=self.screen, settings=self.settings)


    
# Helper Method
    def _key_is_pressed(self, event):
        """When key is pressed."""
        if event.key == pygame.K_RIGHT:
            # Main Screen
            if self.screens.s2:
                self.screens.ship.right =  True
            pass

        elif event.key == pygame.K_LEFT:
            # Main Screen
            if self.screens.s2:
                self.screens.ship.left = True
            pass

    
    def _key_is_released(self, event):
        """When key is pressed."""
        if event.key == pygame.K_RIGHT:
            # Main Screen
            if self.screens.s2:
                self.screens.ship.right = False
            pass

        elif event.key == pygame.K_LEFT:
            # Main Screen
            if self.screens.s2:
                self.screens.ship.left = False
            pass

            
    def _mouse_is_clicked(self, current_pos):
        if self.screens.play.rect.collidepoint(current_pos):
            self.screens._set_screen(s2=True)
            
        pass


# -------------------------------------------



    # Check Event
    def check_event(self):
        """Check Event."""
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._key_is_pressed(event)
                pass
            
            elif event.type == pygame.KEYUP:
                self._key_is_released(event)
                pass

            elif event.type == pygame.MOUSEBUTTONDOWN:
                current_pos = pygame.mouse.get_pos()
                print(current_pos)
                if self.screens.s1:
                   self._mouse_is_clicked(current_pos)
                pass

            # Bullet
    