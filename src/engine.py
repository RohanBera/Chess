import chess
import random
import numpy as np
# Write the engine here

def move(moves):
    move_arr = np.array(moves)
    print(random.choice(move_arr))

def main():
    board = chess.Board()
    m_maker = chess.Move
    while(not board.is_game_over()):
        print(board)
        moves = board.legal_moves
        print("Make your choice according to Chess Notation")
        h_move=board.parse_san(input("As in e4 or d5 etc"))
        if(h_move not in moves):
            print("Make a legal move")
            continue
        board.push(h_move)
        c_move = m_maker.from_uci(str(move(moves)))
        board.push(c_move)
        if(board.is_game_over()):
            print("Game Over")
            break
        if(board.can_claim_threefold_repetition):
            print("Draw by Repetition")
            break
    print("Hope you enjoyed playing. Check out the source code on github")
main()
