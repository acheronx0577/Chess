import pygame
import os

from sound import Sound
from theme import Theme
from const import *


class Config:

    def __init__(self):
        self.themes = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]

        # Background images - ADD THESE LINES
        self.backgrounds = []
        self._add_backgrounds()
        self.bg_idx = 0
        self.background = self.backgrounds[self.bg_idx] if self.backgrounds else None

        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.move_sound = Sound(
            os.path.join('assets/sounds/move.wav'))
        self.capture_sound = Sound(
            os.path.join('assets/sounds/capture.wav'))

    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    def change_background(self):
        if self.backgrounds:
            self.bg_idx += 1
            self.bg_idx %= len(self.backgrounds)
            self.background = self.backgrounds[self.bg_idx]

    def _add_backgrounds(self):
        # Add your background image paths here
        bg_paths = [
            'assets/backgrounds/wood_bg.jpg',
            'assets/backgrounds/marble_bg.jpg',
            'assets/backgrounds/fabric_bg.jpg',
            'assets/backgrounds/space_bg.jpg'
        ]

        for path in bg_paths:
            if os.path.exists(path):
                try:
                    # Load and scale background to fit the board
                    image = pygame.image.load(path)
                    scaled_bg = pygame.transform.scale(image, (WIDTH, HEIGHT))
                    self.backgrounds.append(scaled_bg)
                except:
                    print(f"Could not load background: {path}")

    def _add_themes(self):
        # Use RGBA colors (Red, Green, Blue, Alpha) for transparency
        # Alpha: 0 = fully transparent, 255 = fully opaque

        # Light squares: more transparent (lower alpha)
        # Dark squares: less transparent (higher alpha)
        # Very transparent light squares
        transparent_light = (242, 225, 195, 80)
        # Less transparent dark squares
        transparent_dark = (195, 160, 130, 150)

        # Update all your themes to use RGBA colors:
        light_brown = Theme(transparent_light, transparent_dark,
                            (255, 244, 130, 100), (229, 205, 89, 150), '#D87474', '#D85656')

        # For blue theme - adjust colors but keep transparency
        blue_light = (242, 225, 195, 80)
        blue_dark = (80, 115, 155, 150)
        blue = Theme(blue_light, blue_dark, (143, 207, 247, 100),
                     (63, 139, 211, 150), '#D87474', '#D85656')

        # For gray theme
        gray_light = (242, 225, 195, 80)
        gray_dark = (106, 105, 104, 150)
        gray = Theme(gray_light, gray_dark, (119, 146, 163, 100),
                     (102, 122, 148, 150), '#D87474', '#D85656')

        # For pastel theme
        pastel_light = (242, 225, 195, 80)
        pastel_dark = (200, 180, 215, 150)
        pastel = Theme(pastel_light, pastel_dark, (255, 225, 175, 100),
                       (220, 200, 240, 150), '#D87474', '#D85656')

        # Continue updating themes with RGBA colors...
        emerald_light = (242, 225, 195, 80)
        emerald_dark = (80, 140, 120, 150)
        emerald = Theme(emerald_light, emerald_dark, (160, 220, 180,
                        100), (100, 180, 150, 150), '#D87474', '#D85656')

        burgundy_light = (242, 225, 195, 80)
        burgundy_dark = (140, 80, 90, 150)
        burgundy = Theme(burgundy_light, burgundy_dark, (220, 160,
                                                         170, 100), (180, 100, 120, 150), '#D87474', '#D85656')

        purple_light = (242, 225, 195, 80)
        purple_dark = (130, 100, 180, 150)
        purple = Theme(purple_light, purple_dark, (200, 170, 230, 100),
                       (160, 120, 200, 150), '#D87474', '#D85656')

        teal_light = (242, 225, 195, 80)
        teal_dark = (70, 130, 150, 150)
        teal = Theme(teal_light, teal_dark, (140, 200, 220, 100),
                     (100, 170, 190, 150), '#D87474', '#D85656')

        gold_light = (242, 225, 195, 80)
        gold_dark = (180, 150, 80, 150)
        gold = Theme(gold_light, gold_dark, (240, 210, 120, 100),
                     (200, 170, 100, 150), '#D87474', '#D85656')

        slate_light = (242, 225, 195, 80)
        slate_dark = (100, 120, 140, 150)
        slate = Theme(slate_light, slate_dark, (170, 190, 210, 100),
                      (130, 150, 170, 150), '#D87474', '#D85656')

        # Keep only 12 themes (removed the last 8)
        self.themes = [light_brown, pastel, blue, gray,
                       emerald, burgundy, purple, teal, gold, slate]
