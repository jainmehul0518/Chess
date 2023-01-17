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
    
    def get_label(self):
        return self.square[2][4]

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

    def update_board(self, old_pos, new_pos):
        cur_label = self.squares[old_pos[0]][old_pos[1]].get_label()
        self.squares[old_pos[0]][old_pos[1]].change_label(' ')
        self.squares[new_pos[0]][new_pos[1]].change_label(cur_label)

    def render_board(self):
        rows = ["" for i in range(40)]
        counter = 0
        for i in range(8):
            for j in range(8):
                curSquare = self.squares[i][j]
                for index, line in enumerate(curSquare.square):
                    if (index == 2 and j == 0):
                        rows[counter+index] += str(8-i) + " " + line
                    else:
                        rows[counter+index] += "  " + line
            counter += 5
        rows.append("      A          B          C          D          E          F          G          H    ")
        for line in rows:
            print(line)