from chess.coordinate import Coordinate, Move

class Piece:
    def __init__(self, is_white):
        self.is_white = is_white

    def __str__(self) -> str:
        return ""

    def get_legal_moves(self, board, position):
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

    def get_legal_moves(self, board, position:Coordinate):
        legal_moves = []
        # for white:
        if self.is_white:
            # one forward
            if board.is_empty(Coordinate(position.x, position.y+1)):
                legal_moves.append(Move(position, Coordinate(position.x, position.y+1)))
            # two forward
            if board.is_empty(Coordinate(position.x, position.y+1)) and board.is_empty(Coordinate(position.x, position.y+2)) and position.y == 1:
                legal_moves.append(Move(position, Coordinate(position.x, position.y+2)))
            # right diagonal
            if board.is_piece(Coordinate(position.x+1, position.y+1), 0):
               legal_moves.append(Move(position, Coordinate(position.x+1, position.y+1)))
            # left diagonal
            if board.is_piece(Coordinate(position.x-1, position.y+1), 0):
               legal_moves.append(Move(position, Coordinate(position.x-1, position.y+1)))
            # en_passant
            if Coordinate(position.x-1, position.y) == board.en_passant:
               legal_moves.append(Move(position, Coordinate(position.x-1, position.y+1)))
               
            if Coordinate(position.x+1, position.y) == board.en_passant:
               legal_moves.append(Move(position, Coordinate(position.x+1, position.y+1)))

        # for black:
        else:
            # one forward
            if board.is_empty(Coordinate(position.x, position.y-1)):
                legal_moves.append(Move(position, Coordinate(position.x, position.y-1)))
            # two forward
            if board.is_empty(Coordinate(position.x, position.y-1)) and board.is_empty(Coordinate(position.x, position.y-2)) and position.y == 6:
                legal_moves.append(Move(position, Coordinate(position.x, position.y-2)))
            # right diagonal
            if board.is_piece(Coordinate(position.x+1, position.y-1), 1):
               legal_moves.append(Move(position, Coordinate(position.x+1, position.y-1)))
            # left diagonal
            if board.is_piece(Coordinate(position.x-1, position.y-1), 1):
               legal_moves.append(Move(position, Coordinate(position.x-1, position.y-1)))
            # en_passant
            if Coordinate(position.x-1, position.y) == board.en_passant:
               legal_moves.append(Move(position, Coordinate(position.x-1, position.y-1)))
            if Coordinate(position.x+1, position.y) == board.en_passant:
               legal_moves.append(Move(position, Coordinate(position.x+1, position.y-1)))
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
        
    def get_legal_moves(self, board, position:Coordinate):
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
        from chess.move_generator import MoveGenerator
        legal_moves = []
        # check all possible moves
        for i in range(-1, 2):
            for j in range(-1, 2):
                # skip if King doesn't move at all
                if i == j == 0:
                    continue
                if board.is_empty(Coordinate(position.x + i, position.y + j)) or board.is_piece(Coordinate(position.x + i, position.y + j), not self.is_white):
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
                for move in MoveGenerator.get_all_legal_moves(board, not self.is_white, True):
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
                for move in MoveGenerator.get_all_legal_moves(board, not self.is_white, True):
                    if move.destination == Coordinate(position.x - i, position.y):
                        is_legal = False
            if is_legal:
                legal_moves.append(Move(position, Coordinate(position.x - 2, position.y)))
                legal_moves.append(Move(Coordinate(position.x - 3, position.y), Coordinate(position.x - 1, position.y)))
        return legal_moves