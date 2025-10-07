import pygame

from const import *
from  board import Board
from dragger import Dragger
class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

    # Blit Method

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (242, 225, 195)  # Gold
                else:
                    color = (195, 160, 130)  # light Black

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                #Check if there is piece
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    # All pieces exceot dragger piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size = 80)

                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)
