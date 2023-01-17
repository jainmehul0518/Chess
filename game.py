import pieces
import render

class Game:
    def __init__(self):
        self.character_dict = dict({'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7})
        self.number_set = set([i+1 for i in range(8)])
        self.turn = "White" # chess game starts off with White's move

        self.game_pieces = dict()
        # Kings
        self.game_pieces[(0,4)] = pieces.King(color="White", pos_x = 0, pos_y = 4)
        self.game_pieces[(7,4)] = pieces.King(color="Black", pos_x = 7, pos_y = 4)

        # Rooks
        self.game_pieces[(0,0)] = pieces.Rook(color="White", pos_x = 0, pos_y = 0) 
        self.game_pieces[(7,0)] = pieces.Rook(color="Black", pos_x = 7, pos_y = 0) 
        self.game_pieces[(0,7)] = pieces.Rook(color="White", pos_x = 0, pos_y = 7)
        self.game_pieces[(7,7)] = pieces.Rook(color="Black", pos_x = 7, pos_y = 7) 

        # Knights
        self.game_pieces[(0,1)] = pieces.Knight(color="White", pos_x = 0, pos_y = 1)
        self.game_pieces[(7,1)] = pieces.Knight(color="Black", pos_x = 7, pos_y = 1) 
        self.game_pieces[(0,6)] = pieces.Knight(color="White", pos_x = 0, pos_y = 6) 
        self.game_pieces[(7,6)] = pieces.Knight(color="Black", pos_x = 7, pos_y = 6)

        # Bishops
        self.game_pieces[(0,2)] = pieces.Bishop(color="White", pos_x = 0, pos_y = 2) 
        self.game_pieces[(7,2)] = pieces.Bishop(color="Black", pos_x = 7, pos_y = 2) 
        self.game_pieces[(0,5)] = pieces.Bishop(color="White", pos_x = 0, pos_y = 5) 
        self.game_pieces[(7,5)] = pieces.Bishop(color="Black", pos_x = 7, pos_y = 5) 

        # Queens
        self.game_pieces[(0,3)] = pieces.Queen(color="White", pos_x = 0, pos_y = 3) 
        self.game_pieces[(7,3)] = pieces.Queen(color="Black", pos_x = 7, pos_y = 3)

        # Pawns
        for i in range(8):
            self.game_pieces[(1,i)] = pieces.Pawn(color="White", pos_x = 1, pos_y = i)
            self.game_pieces[(6,i)] = pieces.Pawn(color="Black", pos_x = 6, pos_y = i)

        self.game_board = render.Board(self.game_pieces)
        self.game_board.render_board()
    
    def validate_input(self, cur_pos):
        if (len(cur_pos) != 2):
            return False, "The current position should only be 2 characters. The first character is a letter A-H, and the second character is a number 1-8."
    
        if (cur_pos[0].upper() not in self.character_dict):
            return False, "The first character is not a letter from A-H."
        try:
            cur_num = int(cur_pos[1])
        except:
            return False, "The second character is not a number. Make sure the second character is a number 1-8."

        if (cur_num not in self.number_set):
            return False, "The second character is not a number from 1-8."

        return True, None
    
    def translate_input(self, cur_pos):
        cur_y = self.character_dict[cur_pos[0].upper()]
        cur_x = 8 - int(cur_pos[1])
        return (cur_x, cur_y)

    def get_current_position(self, cur_pos):
        is_valid, err = self.validate_input(cur_pos)
        if not is_valid:
            return err, None
        cur_coord = self.translate_input(cur_pos)
        if (cur_coord in self.game_pieces):
            if (self.game_pieces[cur_coord].color == self.turn):
                return None, cur_coord
                #print("You selected {} {} located at {}, {}".format(self.game_pieces[cur_coord].color, self.game_pieces[cur_coord].label, self.game_pieces[cur_coord].pos_x, self.game_pieces[cur_coord].pos_y))
            else:
                return "Not your piece.", None
        else:
            return "No piece exists at that position.", None

    def get_new_position(self, new_pos):
        is_valid, err = self.validate_input(new_pos)
        if not is_valid:
            return err, None
        new_coord = self.translate_input(new_pos)
        return None, new_coord

    def get_possible_moves(self, cur_coord, new_coord):
        possible_moves = self.game_pieces[cur_coord].possible_moves(self.game_pieces)
        print(possible_moves)
        #print(new_coord)
        # IF NEW_COORD ISN'T IN POSSIBLE_MOVES LIST...
        if not possible_moves or new_coord not in possible_moves:
            return "Invalid Move. Please try again."
        return None

    def move_piece(self, cur_coord, new_coord):
        if new_coord in self.game_pieces: # remove new_coord key entry if present in game_pieces
            del self.game_pieces[new_coord]
        game_piece = self.game_pieces[cur_coord]
        game_piece.move_piece(new_coord)
        del self.game_pieces[cur_coord]
        self.game_pieces[new_coord] = game_piece
        self.game_board.update_board(cur_coord,new_coord)
        self.game_board.render_board()
        print()

    def game_loop(self, cur_coord, new_coord):
        # GET POSSIBLE MOVES FOR CURRENT PIECE
        err = self.get_possible_moves(cur_coord, new_coord)
        if err:
            return err
            
        # MOVE GAME PIECE FROM CURRENT TO NEW POSITION
        self.move_piece(cur_coord, new_coord)

        # SWITCH COLOR
        self.turn = "Black" if self.turn == "White" else "White"

        return None