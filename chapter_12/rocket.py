# Deon Anoth
# 06-26-2025
# Python Crash Course: Try it yourself: 12-4

import sys
import pygame
from settings import Settings


class GameRocket:
    """A class to represent a game with a rocket."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rocket Game")

        self.rocket = Rocket(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._check_keyspressed()
            self.rocket.update()
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

    def _check_keyspressed(self):
        """Check which keys are pressed and update rocket movement."""
        keys = pygame.key.get_pressed()

        # Vertical movement
        if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.rocket.moving_up = True
            self.rocket.moving_down = False
        elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            self.rocket.moving_down = True
            self.rocket.moving_up = False
        else:
            self.rocket.moving_up = False
            self.rocket.moving_down = False

        # Horizontal movement
        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.rocket.moving_left = True
            self.rocket.moving_right = False
        elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.rocket.moving_right = True
            self.rocket.moving_left = False
        else:
            self.rocket.moving_left = False
            self.rocket.moving_right = False
            
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # Draw the rocket to the screen.
        self.rocket.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


class Rocket:
    """A class to manage the rocket."""
    
    def __init__(self, gr_game):
        """Initialize the rocket."""
        self.screen = gr_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = gr_game.settings

        # Load the rocket image and get its rect.
        rocket_image = "chapter_12/images/fighter.bmp"
        self.image = pygame.image.load(rocket_image)
        self.rect = self.image.get_rect()

        # Start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        
    def update(self):
        """Update the rocket's position based on movement flags."""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.settings.speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.speed_factor

        self.x = self.rect.x
        self.y = self.rect.y

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    gr = GameRocket()
    gr.run_game()