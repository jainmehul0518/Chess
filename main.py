import game
import argparse

# GLOBAL VARIABLES
test_script = None

# CLI Argument Parsing
parser = argparse.ArgumentParser()
parser.add_argument('--script', action='store', dest='test_script',help="Specify name of test script file.")
args = parser.parse_args()
test_script = args.test_script

def main():
    chess_game = game.Game()
    if test_script != None:
        with open(test_script,'r') as f:
            commands = [line.strip() for line in f]
        i = 0
        print(commands)
        while (i < len(commands)-1):
            # GET CURRENT POSITION
            cur_pos = commands[i]
            err, cur_coord = chess_game.get_current_position(cur_pos)
            if err:
                i+=1
                continue
            # GET NEW_POSITION
            new_pos = commands[i+1]
            err, new_coord = chess_game.get_new_position(new_pos)
            # CALL GAME LOOP TO EXECUTE POSITION CHANGE
            err = chess_game.game_loop(cur_coord, new_coord)
            i += 2
    else:
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