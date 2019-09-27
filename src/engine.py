import chess
import random
import numpy as np
# Write the engine here

def move(moves):
    move_arr = np.array(moves)
    print(random.choice(move_arr))
def main():
    board = chess.Board()
    moves = board.legal_moves
    print(moves,type(moves))
main()
