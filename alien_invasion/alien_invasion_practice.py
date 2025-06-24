# just for practicing alien invasion example
# chapter 12: alien invasion example
# contains some notes and comments - also refer to the notes.txt in ./alien_invasion directory.

import sys
import pygame


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):                     # initializer/constructor method
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._check_keyspressed()
            self.ship.update()
            self._update_screen()
            # Limit the frame rate to 60 FPS
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypreses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key == pygame.K_a:
                        self.ship.auto_run = True
                        self.ship.auto_run_direction = 'left'
                    elif event.key == pygame.K_d:
                        self.ship.auto_run = True
                        self.ship.auto_run_direction = 'right'
                    elif event.key == pygame.K_s:
                        self.ship.auto_run = False
                        self.ship.moving_left = False
                        self.ship.moving_right = False

    def _check_keyspressed(self):
        """Check which keys are pressed and update ship movement."""
        """Auto run is set to False if a key is pressed."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            # If both left and right keys are pressed, stop movement
            self.ship.moving_left = False
            self.ship.moving_right = False
        elif keys[pygame.K_LEFT]:
            self.ship.auto_run = False
            self.ship.moving_left = True
        elif keys[pygame.K_RIGHT]:
            self.ship.auto_run = False
            self.ship.moving_right = True
        else:
            # If neither arrow key is held, stop movement (but don't affect A/D auto-run)
            self.ship.moving_left = False
            self.ship.moving_right = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 10.0


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # Load the ship image.
        ship_image = "alien_invasion/images/ship.bmp"
        self.image = pygame.image.load(ship_image)
        # Create a rect object for the ship (default position (0, 0)).
        self.rect = self.image.get_rect()
        #You use the image (self.image) for drawing, but you do not rely on its original size and position after creating the rect. Instead, you use the Rect (self.rect) to control the position (and, if needed, the size) of where the image appears on the screen. The image’s pixel data stays the same, but its location on the screen is determined by the current values in self.rect.

        # Set the start position of the ship to midbottom of the screen.
        self.rect.midbottom = self.screen.get_rect().midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Initializing Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        # Initializing Auto-run flags; these will be used for auto-running left or right.
        self.auto_run = False
        self.auto_run_direction = None  # Default direction for auto-run

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Handle auto-run functionality
        elif self.auto_run:
            if self.auto_run_direction == 'left' and self.rect.left > 0:
                self.x -= self.settings.ship_speed
            elif self.auto_run_direction == 'right' and self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed

        # Update the rect object from self.x.
        self.rect.x = self.x
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()