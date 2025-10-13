from chess.pieces import *
from chess.coordinate import Coordinate

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
        # important flags
        self.white_castling_lost = False
        self.black_castling_lost = False
        self.en_passant = None
        self.white_king = Coordinate(4, 0)
        self.black_king = Coordinate(4, 7)


        # piece positions
        self.black_pieces = []
        self.white_pieces = []
        

            
    def __str__(self):
        result = ""
        for y in range(7, -1, -1):
            result += str(y+1) + ' |'
            for x in range(7, -1, -1):
                result += " " + str(self.matrix[y][x])
            result += "\n"
        result += "   ----------------\n    a b c d e f g h\n"
        return result
    
    
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
        # update King position
        if isinstance(self.get_piece(move.destination), King):
            if self.get_piece(move.destination).is_white: # type: ignore
                self.white_king = move.destination
            else:
                self.black_king = move.destination
        # update castling information
        if not self.white_castling_lost and (move.start in [Coordinate(0,0), Coordinate(7,0), Coordinate(3,0)]):
            self.white_castling_lost = True
        if not self.black_castling_lost and (move.start in [Coordinate(0,7), Coordinate(7,7), Coordinate(3,7)]):
            self.black_castling_lost = True

    def move(self, move:Move):
        self.move_helper(move)
        # castling
        if isinstance(self.get_piece(move.destination), King):
            if move == Move(Coordinate(3,0), Coordinate(1,0)):
                self.move_helper(Move(Coordinate(0, 0), Coordinate(2, 0)))
            if move == Move(Coordinate(3,0), Coordinate(5,0)):
                self.move_helper(Move(Coordinate(7, 0), Coordinate(4, 0)))
            if move == Move(Coordinate(3,7), Coordinate(1,7)):
                self.move_helper(Move(Coordinate(0, 7), Coordinate(2, 7)))
            if move == Move(Coordinate(3,7), Coordinate(5,7)):
                self.move_helper(Move(Coordinate(7, 7), Coordinate(4, 7)))
        # check if this move was en_passant
        piece = self.get_piece(move.destination)
        if isinstance(piece, Pawn):
            if piece.is_white:
                if Coordinate(move.destination.x, move.destination.y-1) == self.en_passant:
                    self.set_piece(self.en_passant, EmptyPiece())
            else:
                if Coordinate(move.destination.x, move.destination.y+1) == self.en_passant:
                    self.set_piece(self.en_passant, EmptyPiece())
        # set en_passant flag
        if isinstance(self.get_piece(move.destination), Pawn):
            if move.start.y == 1 and move.destination.y == 3 or move.start.y == 6 and move.destination.y == 4:
                self.en_passant = move.destination
            else:
                self.en_passant = None