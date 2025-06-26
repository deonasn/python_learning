# Deon Anoth
# 06-26-2025
# Python Crash Course: Try it yourself: 12-5

import sys
import pygame
from settings import Settings


class GameKeys:
    """A class to represent a game with a rocket."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Keys Game")


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
    
    def _check_events(self):
        """Respond to keypreses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self._check_keydown(event)

    def _check_keydown(self, event):
        """Check keydown events and update keys movement."""
        if event.key == pygame.K_ESCAPE:
            # Exit the game when the Escape key is pressed.
            sys.exit()
        else:
            # Prints the key pressed.
            print(f"\t-> Key pressed: {pygame.key.name(event.key)}")
            
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    gk = GameKeys()
    gk.run_game()