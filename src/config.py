import pygame
import os

from sound import Sound
from theme import Theme

class Config:

    def __init__(self):
        self.themes = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.move_sound = Sound(
            os.path.join('assets/sounds/move.wav'))
        self.capture_sound = Sound(
            os.path.join('assets/sounds/capture.wav'))

    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]


    def _add_themes(self):
        light_brown = Theme((242, 225, 195), (195, 160, 130), (255, 244, 130), (229, 205, 89), '#D87474', '#D85656')

        blue = Theme((242, 225, 195), (80, 115, 155), (143, 207, 247), (63, 139, 211), '#D87474', '#D85656')

        gray = Theme((242, 225, 195), (106, 105, 104), (119, 146, 163), (102, 122, 148), '#D87474', '#D85656')

        pastel = Theme((242, 225, 195), (200, 180, 215), (255, 225, 175), (220, 200, 240), '#D87474', '#D85656')

        emerald = Theme((242, 225, 195), (80, 140, 120), (160, 220, 180), (100, 180, 150), '#D87474', '#D85656')

        burgundy = Theme((242, 225, 195), (140, 80, 90), (220, 160, 170), (180, 100, 120), '#D87474', '#D85656')

        purple = Theme((242, 225, 195), (130, 100, 180), (200, 170, 230), (160, 120, 200), '#D87474', '#D85656')

        teal = Theme((242, 225, 195), (70, 130, 150), (140, 200, 220), (100, 170, 190), '#D87474', '#D85656')

        gold = Theme((242, 225, 195), (180, 150, 80), (240, 210, 120), (200, 170, 100), '#D87474', '#D85656')

        slate = Theme((242, 225, 195), (100, 120, 140), (170, 190, 210), (130, 150, 170), '#D87474', '#D85656')

        rose = Theme((242, 225, 195), (200, 140, 160), (240, 190, 200), (220, 160, 180), '#D87474', '#D85656')

        forest = Theme((242, 225, 195), (100, 130, 100), (170, 200, 170), (130, 160, 130), '#D87474', '#D85656')

        amethyst = Theme((242, 225, 195), (160, 100, 200), (220, 160, 240), (180, 120, 220), '#D87474', '#D85656')

        magenta_blue = Theme((242, 225, 195), (180, 80, 160), (200, 140, 220), (160, 100, 200), '#D87474', '#D85656')

        violet_red = Theme((242, 225, 195), (170, 90, 170), (220, 140, 200), (190, 110, 180), '#D87474', '#D85656')

        berry_blue = Theme((242, 225, 195), (150, 100, 180), (190, 150, 220), (160, 120, 200), '#D87474', '#D85656')

        sunset = Theme((242, 225, 195), (190, 100, 150), (230, 160, 190), (200, 120, 170), '#D87474', '#D85656')

        neon_fusion = Theme((242, 225, 195), (140, 80, 200), (180, 120, 240), (150, 100, 220), '#D87474', '#D85656')

        royal_blend = Theme((242, 225, 195), (130, 100, 190), (170, 140, 230), (140, 120, 210), '#D87474', '#D85656')

        electric = Theme((242, 225, 195), (160, 70, 180), (200, 110, 220), (170, 90, 200), '#D87474', '#D85656')

        self.themes = [light_brown, pastel, blue, gray, emerald, burgundy, purple, teal, gold, slate, rose, forest, amethyst, magenta_blue, violet_red, berry_blue, sunset, neon_fusion, royal_blend, electric]
