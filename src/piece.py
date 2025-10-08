import os


class Piece:

    def __init__(self, name, color, value):
        self.name = name
        self.color = color

        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.set_texture()  # This sets self.texture
        self.texture_rect = None
        self.moves = []
        self.moved = False

    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )

    def add_move(self, move):
        self.moves.append(move)


class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)  # Removed texture parameter


class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)  # Removed texture parameter


class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.001)  # Removed texture parameter


class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)  # Removed texture parameter


class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)  # Removed texture parameter


class King(Piece):
    def __init__(self, color):
        super().__init__('king', color, 10000.0)  # Removed texture parameter
