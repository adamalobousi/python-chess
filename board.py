from pieces import *

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

    
    def move_helper(self, move: Move):
        self.set_piece(move.destination, self.get_piece(move.start))
        self.set_piece(move.start, EmptyPiece())
        if not self.white_castling_lost and (move.start in [Coordinate(0,0), Coordinate(7,0), Coordinate(3,0)]):
            self.white_castling_lost = True
        if not self.black_castling_lost and (move.start in [Coordinate(0,7), Coordinate(7,7), Coordinate(3,7)]):
            self.black_castling_lost = True

    def move(self, move:Move):
        self.move_helper(move)
        # castling
        if move == Move(Coordinate(3,0), Coordinate(1,0)):
            self.move_helper(Move(Coordinate(0, 0), Coordinate(2, 0)))
        if move == Move(Coordinate(0,0), Coordinate(2,0)):
            self.move_helper(Move(Coordinate(3, 0), Coordinate(1, 0)))
        if move == Move(Coordinate(3,0), Coordinate(5,0)):
            self.move_helper(Move(Coordinate(7, 0), Coordinate(4, 0)))
        if move == Move(Coordinate(7,0), Coordinate(4,0)):
            self.move_helper(Move(Coordinate(3, 0), Coordinate(5, 0)))
        if move == Move(Coordinate(3,7), Coordinate(1,7)):
            self.move_helper(Move(Coordinate(0, 7), Coordinate(2, 7)))
        if move == Move(Coordinate(0,7), Coordinate(2,7)):
            self.move_helper(Move(Coordinate(3, 7), Coordinate(1, 7)))
        if move == Move(Coordinate(3,7), Coordinate(5,7)):
            self.move_helper(Move(Coordinate(7, 7), Coordinate(4, 7)))
        if move == Move(Coordinate(7,7), Coordinate(4,7)):
            self.move_helper(Move(Coordinate(3, 7), Coordinate(5, 7)))