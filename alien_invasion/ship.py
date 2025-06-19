# Deon Anoth
# 06-18-2025
# Python Crash Course: Try it yourself: 12-2 Alien Invasion
# ship.py for alien_invasion.py

import pygame

class Ship:
    """Class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        ship = "images/bomber.bmp"
        self.image = pygame.image.load(ship)
        self.rect = self.image.get_rect()
        
        # Start each new ship at the center of the screen.
        self.rect.center = self.screen.get_rect().center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)