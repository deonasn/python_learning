# Deon Anoth
# 08-23-2025
# Python Crash Course: Try it yourself: 12-6

import sys
import pygame
from pygame.sprite import Sprite


class GameSidewayShooter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):                     # initializer/constructor method
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Sideways Shooter Game")

        self.sws = SidewaysShooter(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._check_keyspressed()
            self.sws.update()
            self._update_bullets()
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
                    elif event.key == pygame.K_SPACE:
                        self._fire_bullet()
                    elif event.key == pygame.K_w:
                        self.sws.auto_run = True
                        self.sws.auto_run_direction = 'up'
                    elif event.key == pygame.K_s:
                        self.sws.auto_run = True
                        self.sws.auto_run_direction = 'down'
                    elif event.key == pygame.K_a:
                        self.sws.auto_run = False
                        self.sws.moving_up = False
                        self.sws.moving_down = False

    def _check_keyspressed(self):
        """Check which keys are pressed and update sideways shooter ship movement."""
        """Auto run is set to False if a key is pressed."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
            # If both up and down keys are pressed, stop vertical movement
            self.sws.moving_up = False
            self.sws.moving_down = False
        elif keys[pygame.K_UP]:
            self.sws.auto_run = False
            self.sws.moving_up = True
        elif keys[pygame.K_DOWN]:
            self.sws.auto_run = False
            self.sws.moving_down = True
        else:
            # If neither arrow key is held, stop vertical movement (but don't affect A/D auto-run)
            self.sws.moving_up = False
            self.sws.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet poistions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
        
        # Prints the number of bullets on screen for debugging
        print(f"Bullets on screen: {len(self.bullets)}", end='\r')
        

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # Redraw all bullets shot from the sideways shooter ship during each pass through the loop.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Redraw the sideways shooter ship during each pass through the loop.
        self.sws.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Sideways shooter ship settings
        self.sws_speed = 10.0

        # Bullet settings
        self.bullet_speed = 20.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3


class SidewaysShooter:
    """A class to manage the sideways shooter ship."""

    def __init__(self, gsws_game):
        """Initialize the sideways shooter ship and set its starting position."""
        self.screen = gsws_game.screen
        self.settings = gsws_game.settings
        self.screen_rect = self.screen.get_rect()

        # Load the sideways shooter ship image.
        sws_image = "chapter_12/images/ship.bmp"
        self.image = pygame.transform.rotate(pygame.image.load(sws_image), -90)
        # Create a rect object for the sideways shooter ship (default position (0, 0)).
        self.rect = self.image.get_rect()

        # Set the start position of the sideways shooter ship to midleft of the screen.
        self.rect.midleft = self.screen.get_rect().midleft

        # Store a float for the sideways shooter ship's exact vertical position.
        self.y = float(self.rect.y)

        # Initializing Movement flags; start with a sideways shooter ship that's not moving.
        self.moving_down = False
        self.moving_up = False
        # Initializing Auto-run flags; these will be used for auto-running left or right.
        self.auto_run = False
        self.auto_run_direction = None  # Default direction for auto-run

    def update(self):
        """Update the sideways shooter ship's position based on the movement flags."""
        # Update the sideways shooter ship's y position using a float for smooth movement.
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.sws_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.sws_speed
        # Handle auto-run functionality
        elif self.auto_run:
            if self.auto_run_direction == 'up' and self.rect.top > self.screen_rect.top:
                self.y -= self.settings.sws_speed
            elif self.auto_run_direction == 'down' and self.rect.bottom < self.screen_rect.bottom:
                self.y += self.settings.sws_speed

        # Update the rect object from self.y.
        self.rect.y = self.y

    def blitme(self):
        """Draw the sideways shooter ship at its current location."""
        self.screen.blit(self.image, self.rect)

class Bullet(Sprite):
    """A class to manage bullets fired from the sideways shooter ship."""

    def __init__(self, gsws_game):
        """Create a bullet object at the sideways shooter ship's current position."""
        super().__init__()
        self.screen = gsws_game.screen
        self.settings = gsws_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = gsws_game.sws.rect.midleft

        # Store the bullet's position as a float.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.x += self.settings.bullet_speed
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    gsws = GameSidewayShooter()
    print(pygame.display.Info())  # Print display info for debugging
    print(f"\t-> Screen size: {gsws.settings.screen_width}x{gsws.settings.screen_height}")
    gsws.run_game()