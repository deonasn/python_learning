# Deon Anoth
# 06-18-2025
# Python Crash Course: Try it yourself: 12-2

import sys
import pygame
from settings import Settings


class GameCharacter:
    """A class to represent a game with a character."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue Sky")

        self.character = Character(self)

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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
            
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # Draw the character to the screen.
        self.character.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


class Character:
    """A class to manage the character."""
    
    def __init__(self, gc_game):
        """Initialize the character."""
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Load the character image and get its rect.
        character_image = "chapter_12/images/character.bmp"
        self.image = pygame.image.load(character_image)
        self.rect = self.image.get_rect()

        # Start each new character at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    gc = GameCharacter()
    gc.run_game()