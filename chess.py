import copy
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}:{self.y}"
    
    def __eq__(self, value: object):
        return isinstance(value, Coordinate) and self.x == value.x and self.y == value.y
    
class Move:
    def __init__(self, start, destination):
        self.start = start
        self.destination = destination
    
    def __str__(self) -> str:
        return str(self.start) + "->" + str(self.destination)

        

class Board:
    def __init__(self):
        self.matrix : list[list[Piece]] = [
        [Rook(1),Knight(1),Bishop(1),King(1),Queen(1),Bishop(1),Knight(1),Rook(1)],
        [Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1)],
        [EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece()],
        [EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece()],
        [EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece()],
        [EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece()],
        [Pawn(0),Pawn(0),Pawn(0),Pawn(0),Pawn(0),Pawn(0),Pawn(0),Pawn(0)],
        [Rook(0),Knight(0),Bishop(0),King(0),Queen(0),Bishop(0),Knight(0),Rook(0)]
        ]

        self.white_castling_lost = False
        self.black_castling_lost = False
            
    def __str__(self):
            result = "    0 1 2 3 4 5 6 7\n   ----------------\n"
            for y in range(8):
                result += str(y) + ' |'
                for x in range(8):
                    result += " " + str(self.matrix[y][x])
                result += "\n"
            return result
    

    def get_all_legal_moves(self, is_white, ignore_king = False):
        legal_moves = []
        for i in range(8):
            for j in range(8):
                position = Coordinate(i, j)
                piece = self.get_piece(position)
                if self.is_piece(position, is_white):
                    if not ignore_king or not isinstance(piece, King):
                        legal_moves += piece.get_legal_moves(self, position) # type: ignore
        return legal_moves
    
    def is_out_of_bounce(self, position):
            return not position.x in range(8) or not position.y in range(8)  
    
    def is_piece(self, position, is_white = None):
        if self.is_out_of_bounce(position):
            return False
        elif isinstance(self.get_piece(position), EmptyPiece):
            return False
        elif is_white == None:
            return True
        elif not is_white and self.get_piece(position).is_white: # type: ignore
            return False
        elif is_white and not self.get_piece(position).is_white: # type:ignore
            return False
        else:
            return True
            
    def is_empty(self, position):
        if self.is_out_of_bounce(position):
            return False
        elif isinstance(self.get_piece(position), EmptyPiece):
            return True
        else: return False
    
    def get_piece(self, position):
        if self.is_out_of_bounce(position):
            return None
        return self.matrix[position.y][position.x]
    
    def set_piece(self, position, piece):
        if self.is_out_of_bounce(position):
            return
        self.matrix[position.y][position.x] = piece

            

class Piece:
    def __init__(self, is_white):
        self.is_white = is_white

    def __str__(self) -> str:
        return ""

    def get_legal_moves(self, board:Board, position):
        return []
    

class EmptyPiece(Piece):
    def __init__(self):
        super().__init__(None)

    def __str__(self):
        return "*"
    
    

class Pawn(Piece):
    def __str__(self):
        if self.is_white: 
            return 'P'
        else:
            return 'p'

    def get_legal_moves(self, board:Board, position:Coordinate):
        legal_moves = []
        # for white:
        if self.is_white:
            # one forward
            if board.is_empty(Coordinate(position.x, position.y+1)):
                legal_moves.append(Move(position, Coordinate(position.x, position.y+1)))
            # two forward
            if board.is_empty(Coordinate(position.x, position.y+1)) and board.is_empty(Coordinate(position.x, position.y+2)):
                legal_moves.append(Move(position, Coordinate(position.x, position.y+2)))
            # right diagonal
            if board.is_piece(Coordinate(position.x+1, position.y+1), 0):
               legal_moves.append(Move(position, Coordinate(position.x+1, position.y+1)))
            # left diagonal
            if board.is_piece(Coordinate(position.x-1, position.y+1), 0):
               legal_moves.append(Move(position, Coordinate(position.x-1, position.y+1)))
        # for black:
        else:
            # one forward
            if board.is_empty(Coordinate(position.x, position.y-1)):
                legal_moves.append(Move(position, Coordinate(position.x, position.y-1)))
            # two forward
            if board.is_empty(Coordinate(position.x, position.y-1)) and board.is_empty(Coordinate(position.x, position.y-2)):
                legal_moves.append(Move(position, Coordinate(position.x, position.y-2)))
            # right diagonal
            if board.is_piece(Coordinate(position.x+1, position.y-1), 1):
               legal_moves.append(Move(position, Coordinate(position.x+1, position.y-1)))
            # left diagonal
            if board.is_piece(Coordinate(position.x-1, position.y-1), 1):
               legal_moves.append(Move(position, Coordinate(position.x-1, position.y-1)))
        return legal_moves
    
    
class Rook(Piece):
    def __str__(self):
        if self.is_white: 
            return 'R'
        else:
            return 'r'

    def get_legal_moves(self, board, position):
        legal_moves = []
        # all directions
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x+n, position.y))):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y)))
            elif (board.is_piece(Coordinate(position.x+n, position.y), not self.is_white)):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y)))
                break
            else: 
                break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x-n, position.y))):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y)))
            elif (board.is_piece(Coordinate(position.x-n, position.y), not self.is_white)):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x, position.y+n))):
                legal_moves.append(Move(position, Coordinate(position.x, position.y+n)))
            elif (board.is_piece(Coordinate(position.x, position.y+n), not self.is_white)):
                legal_moves.append(Move(position, Coordinate(position.x, position.y+n)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x, position.y-n))):
                legal_moves.append(Move(position, Coordinate(position.x, position.y-n)))
            elif (board.is_piece(Coordinate(position.x, position.y-n), not self.is_white)):
                legal_moves.append(Move(position, Coordinate(position.x, position.y-n)))
                break
            else: break
        return legal_moves
    
    
class Knight(Piece):
    def __str__(self):
        if self.is_white: 
            return 'N'
        else:
            return 'n'
        
    def get_legal_moves(self, board:Board, position:Coordinate):
        legal_moves = []
        # check all possibilities
        if board.is_empty(Coordinate(position.x + 2, position.y + 1)) or board.is_piece(Coordinate(position.x + 2, position.y + 1), not self.is_white):
            legal_moves.append(Move(position, Coordinate(position.x + 2, position.y + 1)))
        if board.is_empty(Coordinate(position.x - 2, position.y + 1)) or board.is_piece(Coordinate(position.x - 2, position.y + 1), not self.is_white):
            legal_moves.append(Move(position, Coordinate(position.x - 2, position.y + 1)))
        if board.is_empty(Coordinate(position.x + 2, position.y - 1)) or board.is_piece(Coordinate(position.x + 2, position.y - 1), not self.is_white):
            legal_moves.append(Move(position, Coordinate(position.x + 2, position.y - 1)))
        if board.is_empty(Coordinate(position.x - 2, position.y - 1)) or board.is_piece(Coordinate(position.x - 2, position.y - 1), not self.is_white):
            legal_moves.append(Move(position, Coordinate(position.x - 2, position.y - 1)))
        if board.is_empty(Coordinate(position.x + 1, position.y + 2)) or board.is_piece(Coordinate(position.x + 1, position.y + 2), not self.is_white):
            legal_moves.append(Move(position, Coordinate(position.x + 1, position.y + 2)))
        if board.is_empty(Coordinate(position.x - 1, position.y + 2)) or board.is_piece(Coordinate(position.x - 1, position.y + 2), not self.is_white):
            legal_moves.append(Move(position, Coordinate(position.x - 1, position.y + 2)))
        if board.is_empty(Coordinate(position.x + 1, position.y - 2)) or board.is_piece(Coordinate(position.x + 1, position.y - 2), not self.is_white):
            legal_moves.append(Move(position, Coordinate(position.x + 1, position.y - 2)))
        if board.is_empty(Coordinate(position.x - 1, position.y - 2)) or board.is_piece(Coordinate(position.x - 1, position.y - 2), not self.is_white):
            legal_moves.append(Move(position, Coordinate(position.x - 1, position.y - 2)))
        return legal_moves
    
    
class Bishop(Piece):
    def __str__(self):
        if self.is_white: 
            return 'B'
        else:
            return 'b'

    def get_legal_moves(self, board:Board, position):
        legal_moves = []
        # all directions
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x+n, position.y+n))):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y+n)))
            elif (board.is_piece(Coordinate(position.x+n, position.y+n), not self.is_white)):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y+n)))
                break
            else: 
                break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x-n, position.y+n))):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y+n)))
            elif (board.is_piece(Coordinate(position.x-n, position.y+n), not self.is_white)):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y+n)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x+n, position.y-n))):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y-n)))
            elif (board.is_piece(Coordinate(position.x+n, position.y-n), not self.is_white)):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y-n)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x-n, position.y-n))):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y-n)))
            elif (board.is_piece(Coordinate(position.x-n, position.y-n), not self.is_white)):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y-n)))
                break
            else: break
        return legal_moves
    
    
class Queen(Piece):
    def __str__(self):
        if self.is_white: 
            return 'Q'
        else:
            return 'q'
        
    def get_legal_moves(self, board, position):
        legal_moves = []
        # all directions
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x+n, position.y+n))):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y+n)))
            elif (board.is_piece(Coordinate(position.x+n, position.y+n), not self.is_white)):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y+n)))
                break
            else: 
                break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x-n, position.y+n))):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y+n)))
            elif (board.is_piece(Coordinate(position.x-n, position.y+n), not self.is_white)):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y+n)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x+n, position.y-n))):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y-n)))
            elif (board.is_piece(Coordinate(position.x+n, position.y-n), not self.is_white)):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y-n)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x-n, position.y-n))):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y-n)))
            elif (board.is_piece(Coordinate(position.x-n, position.y-n), not self.is_white)):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y-n)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x+n, position.y))):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y)))
            elif (board.is_piece(Coordinate(position.x+n, position.y), not self.is_white)):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y)))
                break
            else: 
                break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x-n, position.y))):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y)))
            elif (board.is_piece(Coordinate(position.x-n, position.y), not self.is_white)):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x, position.y+n))):
                legal_moves.append(Move(position,Coordinate(position.x, position.y+n)))
            elif (board.is_piece(Coordinate(position.x, position.y+n), not self.is_white)):
                legal_moves.append(Move(position,Coordinate(position.x, position.y+n)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x, position.y-n))):
                legal_moves.append(Move(position,Coordinate(position.x, position.y-n)))
            elif (board.is_piece(Coordinate(position.x, position.y-n), not self.is_white)):
                legal_moves.append(Move(position,Coordinate(position.x, position.y-n)))
                break
            else: break
        return legal_moves 
    
    
class King(Piece):
    def __str__(self):
        if self.is_white: 
            return 'K'
        else:
            return 'k'

    def get_legal_moves(self, board, position):
        legal_moves = []
        # check all possible moves
        for i in range(-1, 2):
            for j in range(-1, 2):
                # skip if King doesn't move at all
                if i == j == 0:
                    continue
                if board.is_empty(Coordinate(position.x + i, position.y + j)) or board.is_piece(Coordinate(position.x + i, position.y + j), not self.is_white):
                    # simulate this move on a new board
                    simulation_board = copy.deepcopy(board)
                    simulation_board.set_piece(position, EmptyPiece())
                    simulation_board.set_piece(Coordinate(position.x + i, position.y + j), self)
                    # check if destination is a threatend square
                    is_legal = True
                    for move in simulation_board.get_all_legal_moves(not self.is_white, True):
                        if move.destination == Coordinate(position.x + i, position.y + j):
                            is_legal = False
                    if is_legal:
                        legal_moves.append(Move(position, Coordinate(position.x + i, position.y + j)))
        # check long castling
        if (not board.white_castling_lost and self.is_white) or (not board.black_castling_lost and not self.is_white):
            is_legal = True
            #check if its empty
            for i in range(1, 4):
                if not board.is_empty(Coordinate(position.x+i, position.y)):
                    is_legal = False
                    break
            # check if threatend square
            for i in range(0, 5):
                for move in board.get_all_legal_moves(not self.is_white, True):
                    if move.destination == Coordinate(position.x + i, position.y):
                        is_legal = False
            if is_legal:
                legal_moves.append(Move(position, Coordinate(position.x + 2, position.y)))
                legal_moves.append(Move(Coordinate(position.x + 4, position.y), Coordinate(position.x + 1, position.y)))
        # check short castling
        if (not board.white_castling_lost and self.is_white) or (not board.black_castling_lost and not self.is_white):
            is_legal = True
            #check if its empty
            for i in range(1, 3):
                if not board.is_empty(Coordinate(position.x-i, position.y)):
                    is_legal = False
                    break
            # check if threatend square
            for i in range(0, 4):
                for move in board.get_all_legal_moves(not self.is_white, True):
                    if move.destination == Coordinate(position.x - i, position.y):
                        is_legal = False
            if is_legal:
                legal_moves.append(Move(position, Coordinate(position.x - 2, position.y)))
                legal_moves.append(Move(Coordinate(position.x - 3, position.y), Coordinate(position.x - 1, position.y)))
        return legal_moves


class Game:
    def __init__(self):
        self.board = Board()
        self.white_turn = 1




board = Board()
all_moves = board.get_all_legal_moves(1)
for moves in all_moves:
    print(str(moves))
print(str(board))