import pieces

class Square:
    def __init__(self,piece_label="P"):
        self.square = [" ------- ",
                       "|       |",
                       "|       |",
                       "|       |",
                       " ------- "]
        self.square[2] = "|   " + piece_label + "   |"

    def change_label(self,piece_label):
        self.square[2] = "|   " + piece_label + "   |"

class Board:
    def __init__(self, game_pieces):
        self.squares = [[] for i in range(8)]
        for i in range(8):
            for j in range(8):
                if (i, j) in game_pieces:
                    piece_label = game_pieces[(i,j)].label
                else:
                    piece_label = " "
                self.squares[i].append(Square(piece_label))

    def render_board(self):
        rows = ["" for i in range(40)]
        counter = 0
        for i in range(8):
            for j in range(8):
                curSquare = self.squares[i][j]
                for index, line in enumerate(curSquare.square):
                    rows[counter+index] += line
            counter += 5
        for line in rows:
            print(line)

def main():
    game_pieces = dict()
    # Kings
    game_pieces[(0,4)] = pieces.King(color="White", pos_x = 0, pos_y = 4)
    game_pieces[(7,4)] = pieces.King(color="Black", pos_x = 7, pos_y = 4)

    # Rooks
    game_pieces[(0,0)] = pieces.Rook(color="White", pos_x = 0, pos_y = 0) 
    game_pieces[(7,0)] = pieces.Rook(color="Black", pos_x = 7, pos_y = 0) 
    game_pieces[(0,7)] = pieces.Rook(color="White", pos_x = 0, pos_y = 7)
    game_pieces[(7,7)] = pieces.Rook(color="Black", pos_x = 7, pos_y = 7) 

    # Knights
    game_pieces[(0,1)] = pieces.Knight(color="White", pos_x = 0, pos_y = 1) 
    game_pieces[(7,1)] = pieces.Knight(color="Black", pos_x = 7, pos_y = 1) 
    game_pieces[(0,6)] = pieces.Knight(color="White", pos_x = 0, pos_y = 6) 
    game_pieces[(7,6)] = pieces.Knight(color="Black", pos_x = 7, pos_y = 6)

    # Bishops
    game_pieces[(0,2)] = pieces.Bishop(color="White", pos_x = 0, pos_y = 2) 
    game_pieces[(7,2)] = pieces.Bishop(color="Black", pos_x = 7, pos_y = 2) 
    game_pieces[(0,5)] = pieces.Bishop(color="White", pos_x = 0, pos_y = 5) 
    game_pieces[(7,5)] = pieces.Bishop(color="Black", pos_x = 7, pos_y = 5) 

    # Queens
    game_pieces[(0,3)] = pieces.Queen(color="White", pos_x = 0, pos_y = 3) 
    game_pieces[(7,3)] = pieces.Queen(color="Black", pos_x = 7, pos_y = 3) 

    # Pawns
    for i in range(8):
        game_pieces[(1,i)] = pieces.Pawn(color="White", pos_x = 1, pos_y = i)
        game_pieces[(6,i)] = pieces.Pawn(color="Black", pos_x = 6, pos_y = i)

    game_board = Board(game_pieces)
    game_board.render_board()

if __name__ == "__main__":
    main()