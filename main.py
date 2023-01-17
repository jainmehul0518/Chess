import game

def main():
    chess_game = game.Game()
    while True:
        # GET CURRENT POSITION
        cur_pos = input("Please enter the position of the piece you want to move as follows: (Letter A-H)(Number 1-8): ")
        err, cur_coord = chess_game.get_current_position(cur_pos)
        if err != "":
            print(err)
            continue
        # GET NEW_POSITION
        new_pos = input("Please enter the position you want to move the piece to: ")
        err, new_coord = chess_game.get_new_position(new_pos)
        if err != "":
            print(err)
            continue
        # CALL GAME LOOP TO EXECUTE POSITION CHANGE
        err = chess_game.game_loop(cur_coord, new_coord)
        if err != "":
            print(err)

if __name__ == "__main__":
    main()