# just for practicing alien invasion example
# chapter 12: alien invasion example
# contains some notes and comments - also refer to the notes.txt in ./alien_invasion directory.

import sys
import pygame
from pygame.sprite import Sprite


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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._check_keyspressed()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
        
        # if keys[pygame.K_SPACE]:
        #     # Fires bullet continuously if space is held down
        #     self._fire_bullet()

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
        # Use .copy() so we can safely remove bullets from the original group while iterating.
        # If we looped directly over self.bullets, removing items would change the group size and break the loop.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
        
        # Prints the number of bullets on screen for debugging
        print(f"Bullets on screen: {len(self.bullets)}", end='\r')

    def _create_fleet(self):
        """Create the fleet of alien."""
        # Create an alien and keep adding alienss until there's no room left.
        # Spacing between each alien is equal to one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien.x = x_position
        alien.rect.x = x_position
        alien.rect.y = y_position
        self.aliens.add(alien)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # Redraw all bullets shot from the ship during each pass through the loop.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Redraw the ship during each pass through the loop.
        self.ship.blitme()
        # Draw the alien
        self.aliens.draw(self.screen)

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

        # Bullet settings
        self.bullet_speed = 20.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # Load the ship image.
        ship_image = "chapter_12/images/ship.bmp"
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
        # For left/right movement, using two if statements allows both to run (and cancel out).
        # For left/right/auto-run, using if/elif/elif ensures only one movement per frame, which is clearer and avoids bugs.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        # Handle auto-run functionality
        elif self.auto_run:
            if self.auto_run_direction == 'right' and self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
            elif self.auto_run_direction == 'left' and self.rect.left > self.screen_rect.left:
                self.x -= self.settings.ship_speed

        # Update the rect object from self.x.
        self.rect.x = self.x
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

class Bullet(Sprite):
    """A class to manage bullets frired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        alien_image = "chapter_12/images/alien.bmp"
        self.image = pygame.image.load(alien_image)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right or self.rect.left <= 0)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    print(pygame.display.Info())  # Print display info for debugging
    print(f"\t-> Screen size: {ai.settings.screen_width}x{ai.settings.screen_height}")
    ai.run_game()