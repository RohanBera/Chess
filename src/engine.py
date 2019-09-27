import chess
import random
import numpy as np
# Write the engine here

def move(moves):
#    move_arr = np.array(moves)
    move_arr = list(moves)
#    print(random.choice(move_arr))
    return random.choice(move_arr)

def maker(board,m_maker):
    while(not board.is_game_over()):
            print(board)
            moves = board.legal_moves
            print("Make your choice according to Chess Notation")
            h_move=board.parse_san(input("As in e4 or d5 etc\t"))
            if(h_move not in moves):
                print("Make a legal move")
                continue
            board.push(h_move)
            c_move = m_maker.from_uci(str(move(moves)))
            board.push(c_move)
            if(board.is_game_over()):
                print("Game Over")
                break

def main():
    board = chess.Board()
    m_maker = chess.Move
    try:
        maker(board,m_maker)
            #if(board.can_claim_threefold_repetition):
            #    print("Draw by Repetition")
            #    break
    except KeyboardInterrupt:
        print("\nQuitting your game. Bye\n")
    except ValueError:
        print("You entered an illegal move try again")
        try:
            board.pop()
        except IndexError:
            maker(board,m_maker)
    except IndexError:
        maker(board,m_maker)
    print("\nHope you enjoyed playing. Check out the source code on github\n")
main()
