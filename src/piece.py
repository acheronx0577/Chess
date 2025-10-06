
class Piece:
    
    def __init__(self, name, color,  value, texture, texture_rect=None):
        pass

class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)

class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.001)

class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)

class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)

class King(Piece):
    def __init__(self, color):
        super().__init__('king', color, 10000.0)
