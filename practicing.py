# just for practicing while reading
# mostly in-text examples
# chapter 12: alien invasion example

import sys
import pygame


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):                     # initializer/constructor method
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            # Limit the frame rate to 60 FPS
            self.clock.tick(60)


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Load the ship image and get its rect.
        # ship_image = "alien_invasion/images/3B.bmp"
        # ship_image = "alien_invasion/images/battlecruiser.bmp"
        # ship_image = "alien_invasion/images/bomber.bmp"
        # ship_image = "alien_invasion/images/scout.bmp"
        ship_image = "alien_invasion/images/ship.bmp"
        self.image = pygame.image.load(ship_image)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen.get_rect().midbottom
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()