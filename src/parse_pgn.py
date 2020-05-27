def parse(file):
    with open(file) as pgn_file:
        game_moves = []
        for line in pgn_file:
            if line.startswith('1. '):
                game_moves.append(line)
    return game_moves
