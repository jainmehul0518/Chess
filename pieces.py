class Piece:
    def __init__(self, color="White", pos_x=0, pos_y=0):
        self.color = color # Assume that white is top of board, black is bottom of board
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.taken = False
        self.label = "P"
    def possible_moves(self, game_pieces):
        pass
    def move_piece(self):
        pass

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
        self.has_moved = False
        self.label = "P"

    def possible_moves(self, game_pieces):
        move_dir = 1 if self.color == "White" else -1
        possible_moves = []

        # piece can move 1 square in move_dir
        if (self.pos_x + move_dir, self.pos_y) not in game_pieces:
            possible_moves.append((self.pos_x + move_dir, self.pos_y))
        # if piece hasn't moved in game, can move 2 squares
        if not self.has_moved and (self.pos_x + (2*move_dir), self.pos_y) not in game_pieces:
            possible_moves.append((self.pos_x + (2*move_dir), self.pos_y))
        
        diagonal_1 = (self.pos_x + move_dir, self.pos_y + move_dir)
        diagonal_2 = (self.pos_x + move_dir, self.pos_y - move_dir)
        if diagonal_1 in game_pieces and game_pieces[diagonal_1].color != self.color:
            possible_moves.append(diagonal_1)
        if diagonal_2 in game_pieces and game_pieces[diagonal_2].color != self.color:
            possible_moves.append(diagonal_2)
        
        return possible_moves

    def move_piece(self, new_pos):
        self.pos_x, self.pos_y = new_pos[0], new_pos[1]
        self.has_moved = True