class Piece:
    def __init__(self, color="White", pos_x=0, pos_y=0):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.taken = False
        self.label = "P"

class King(Piece):
    def __init__(self, color="White", pos_x=0, pos_y=0):
        super().__init__(color, pos_x, pos_y)
        self.label = "K"

class Queen(Piece):
    def __init__(self, color="White", pos_x=0, pos_y=0):
        super().__init__(color, pos_x, pos_y)
        self.label = "Q"

class Rook(Piece):
    def __init__(self, color="White", pos_x=0, pos_y=0):
        super().__init__(color, pos_x, pos_y)
        self.label = "R"

class Bishop(Piece):
    def __init__(self, color="White", pos_x=0, pos_y=0):
        super().__init__(color, pos_x, pos_y)
        self.label = "B"

class Knight(Piece):
    def __init__(self, color="White", pos_x=0, pos_y=0):
        super().__init__(color, pos_x, pos_y)
        self.label = "N"

class Pawn(Piece):
    def __init__(self, color="White", pos_x=0, pos_y=0):
        super().__init__(color, pos_x, pos_y)
        self.label = "P"
