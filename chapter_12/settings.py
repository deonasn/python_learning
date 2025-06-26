# Deon Anoth
# 06-18-2025
# Python Crash Course: Try it yourself: Chapter 12
# settings.py for Chapter 12

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.speed_factor = 10.0