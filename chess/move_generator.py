import copy
from coordinate import Coordinate
from chess.pieces import *
from chess.pieces import King

class MoveGenerator:
    @staticmethod
    def get_all_legal_moves(board, is_white, prevent_recursion = False):
        legal_moves = []
        for coord, piece in (board.white_pieces if is_white else board.black_pieces).items():
                position = coord
                piece = piece        
                if not prevent_recursion or not isinstance(piece, King):
                    legal_moves += piece.get_legal_moves(board, position) # type: ignore
        # simulate moves on a new board
        if not prevent_recursion:
            legal_moves = [move for move in legal_moves if not MoveGenerator.simulate_and_check_if_check(board, move)]
        return legal_moves
    
    @staticmethod
    def simulate_and_check_if_check(board, move:Move):
        piece_captured = board.get_piece(move.destination)
        # save board states
        black_castling_lost = board.black_castling_lost
        white_castling_lost = board.white_castling_lost
        en_passant = board.en_passant
        white_king = board.white_king
        black_king = board.black_king
        king_position = white_king if board.get_piece(move.start).is_white else black_king
        # move
        board.move(move)

        # check if destination is a threatend square
        is_check = False
        for legal_move in MoveGenerator.get_all_legal_moves(board, not board.get_piece(move.start).is_white, True):  # type: ignore
            if legal_move.destination == king_position:
                is_check = True
                break

        # move back
        board.set_piece(move.start, board.get_piece(move.destination))
        board.set_piece(move.destination, piece_captured)
        # castling back
        if isinstance(board.get_piece(move.start), King):
            if move == Move(Coordinate(3,0), Coordinate(1,0)):
                board.move_helper(Move(Coordinate(2, 0), Coordinate(0, 0)))
            if move == Move(Coordinate(3,0), Coordinate(5,0)):
                board.move_helper(Move(Coordinate(4, 0), Coordinate(7, 0)))
            if move == Move(Coordinate(3,7), Coordinate(1,7)):
                board.move_helper(Move(Coordinate(2, 7), Coordinate(0, 7)))
            if move == Move(Coordinate(3,7), Coordinate(5,7)):
                board.move_helper(Move(Coordinate(4, 7), Coordinate(7, 7)))
        # en_passante back
        if en_passant != None:
            if isinstance(board.get_piece(en_passant), EmptyPiece):
                board.set_piece(en_passant, Pawn(not Pawn(board.get_piece(move.start).is_white)))
        # reset board states
        board.black_castling_lost = black_castling_lost
        board.white_castling_lost = white_castling_lost
        board.en_passant = en_passant
        board.black_king = black_king
        board.white_king = white_king
        return is_check
