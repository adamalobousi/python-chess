from board import Board
from coordinate import Coordinate, Move
from pieces import *

class Game:
    def __init__(self):
        self.board = Board()
        self.white_turn = 1



    

    def make_move(self, move_string = None):
        try:
            if move_string == None:
                xs, ys, xd, yd = map(int, input("enter move:"))
            else:
                xs, ys, xd, yd = map(int, move_string)
        except:
            print("invalid input")
            return False
        start = Coordinate(xs, ys)
        destination = Coordinate(xd, yd)
        move = Move(start, destination)
        all_moves = self.board.get_all_legal_moves(self.white_turn)
        if move in all_moves:
            self.board.move(move)
            return True
        return False
        

    def play_round(self):
        while True:
            while not self.make_move():
                print("illegal move")
            print(str(self.board))
            self.white_turn = not self.white_turn



    def play_automated_round(self, list):
        for n in list:
            if not self.make_move(n):
                print("illegal move")
            print(str(self.board))
            self.white_turn = not self.white_turn



