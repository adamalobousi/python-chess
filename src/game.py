from src.board import Board
from src.coordinate import Coordinate, Move
from src.pieces import *

class Game:
    def __init__(self):
        self.board = Board()
        self.white_turn = 1

    def make_move(self, move_string = None):
        try:
            if move_string == None:
                if self.white_turn:
                    xs, ys, xd, yd = map(str, input("White's turn. Enter move:"))
                else:
                    xs, ys, xd, yd = map(str, input("Black's turn. Enter move:"))
                print()
            else:
                xs, ys, xd, yd = map(str, move_string)
        except:
            return False
        xs = 7 - ((ord(xs) - 97))
        ys = int(ys) - 1
        xd = 7 - (ord(xd) - 97)
        yd = int(yd) - 1
        start = Coordinate(xs, ys)
        destination = Coordinate(xd, yd)
        move = Move(start, destination)
        all_moves = self.board.get_all_legal_moves(self.white_turn)
        if move in all_moves:
            self.board.move(move)
            return True
        return False
        

    def play_round(self):
        print("-------------------")
        print("Game started")
        print()
        print(self.board)
        while True:
            if self.board.get_all_legal_moves == []:
                if self.white_turn:
                    print("Checkmate! Black wins")
                else: print("Checkmate! White wins")
                break
            while not self.make_move():
                print("Illegal move. Enter again")
            print(str(self.board))
            self.white_turn = not self.white_turn



    def play_automated_round(self, list):
        for n in list:
            print(str(n))
            if not self.make_move(n):
                print("illegal move")
            else: 
                print(str(self.board))
                self.white_turn = not self.white_turn
            if self.board.get_all_legal_moves == []:
                print("checkmate!")
                break