# Deon Anoth
# 06-17-2025
# Python Crash Course: Try it yourself: 12-1

import sys
import pygame

class BlueSky:
    """A class to manage the game resources and behavior for a simple blue sky game."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1280, 720))  # Set the screen size to 1280x720
        pygame.display.set_caption("Blue Sky")

        self.bg_color = (135, 206, 235)  # Set the background color to sky blue

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            # Limit the frame rate to 60 FPS
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypreses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    bs = BlueSky()
    bs.run_game()