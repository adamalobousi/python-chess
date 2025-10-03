from board import Board
board = Board()
all_moves = board.get_all_legal_moves(1)
for moves in all_moves:
    print(str(moves))
print(str(board))