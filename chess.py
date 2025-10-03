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
        [Rook(1),Knight(1),Bishop(1),Knight(1),Queen(1),Bishop(1),Knight(1),Rook(1)],
        [Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1)],
        [EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece()],
        [EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece()],
        [EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece()],
        [EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece(),EmptyPiece()],
        [Pawn(0),Pawn(0),Pawn(0),Pawn(0),Pawn(0),Pawn(0),Pawn(0),Pawn(0)],
        [Rook(0),Knight(0),Bishop(0),Knight(0),Queen(0),Bishop(0),Knight(0),Rook(0)]
        ]
            
    def __str__(self):
            result = "    0 1 2 3 4 5 6 7\n   ----------------\n"
            for y in range(8):
                result += str(y) + ' |'
                for x in range(8):
                    result += " " + str(self.matrix[y][x])
                result += "\n"
            return result
    

    def get_all_legal_moves(self, isWhite):
        legal_moves = []
        for i in range(8):
            for j in range(8):
                position = Coordinate(i, j)
                piece = self.get_piece(position)
                if self.is_piece(position, isWhite):
                    legal_moves += piece.get_legal_moves(self, position) # type: ignore
        return legal_moves
    
    def is_out_of_bounce(self, position):
            return not position.x in range(8) or not position.y in range(8)  
    
    def is_piece(self, position, isWhite = None):
        if self.is_out_of_bounce(position):
            return False
        elif isinstance(self.get_piece(position), EmptyPiece):
            return False
        elif isWhite == None:
            return True
        elif not isWhite and self.get_piece(position).isWhite: # type: ignore
            return False
        elif isWhite and not self.get_piece(position).isWhite: # type:ignore
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
    def __init__(self, isWhite):
        self.isWhite = isWhite

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
        if self.isWhite: 
            return 'P'
        else:
            return 'p'

    def get_legal_moves(self, board:Board, position:Coordinate):
        legal_moves = []
        # for white:
        if self.isWhite:
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
        if self.isWhite: 
            return 'R'
        else:
            return 'r'

    def get_legal_moves(self, board, position):
        legal_moves = []
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x+n, position.y))):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y)))
            elif (board.is_piece(Coordinate(position.x+n, position.y), not self.isWhite)):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y)))
                break
            else: 
                break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x-n, position.y))):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y)))
            elif (board.is_piece(Coordinate(position.x-n, position.y), not self.isWhite)):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x, position.y+n))):
                legal_moves.append(Move(position, Coordinate(position.x, position.y+n)))
            elif (board.is_piece(Coordinate(position.x, position.y+n), not self.isWhite)):
                legal_moves.append(Move(position, Coordinate(position.x, position.y+n)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x, position.y-n))):
                legal_moves.append(Move(position, Coordinate(position.x, position.y-n)))
            elif (board.is_piece(Coordinate(position.x, position.y-n), not self.isWhite)):
                legal_moves.append(Move(position, Coordinate(position.x, position.y-n)))
                break
            else: break
        return legal_moves
    
    
class Knight(Piece):
    def __str__(self):
        if self.isWhite: 
            return 'N'
        else:
            return 'n'
        
    def get_legal_moves(self, board:Board, position:Coordinate):
        legal_moves = []
        # alle möglichkeiten prüfen
        if board.is_empty(Coordinate(position.x + 2, position.y + 1)) or board.is_piece(Coordinate(position.x + 2, position.y + 1), not self.isWhite):
            legal_moves.append(Move(position, Coordinate(position.x + 2, position.y + 1)))
        if board.is_empty(Coordinate(position.x - 2, position.y + 1)) or board.is_piece(Coordinate(position.x - 2, position.y + 1), not self.isWhite):
            legal_moves.append(Move(position, Coordinate(position.x - 2, position.y + 1)))
        if board.is_empty(Coordinate(position.x + 2, position.y - 1)) or board.is_piece(Coordinate(position.x + 2, position.y - 1), not self.isWhite):
            legal_moves.append(Move(position, Coordinate(position.x + 2, position.y - 1)))
        if board.is_empty(Coordinate(position.x - 2, position.y - 1)) or board.is_piece(Coordinate(position.x - 2, position.y - 1), not self.isWhite):
            legal_moves.append(Move(position, Coordinate(position.x - 2, position.y - 1)))
        if board.is_empty(Coordinate(position.x + 1, position.y + 2)) or board.is_piece(Coordinate(position.x + 1, position.y + 2), not self.isWhite):
            legal_moves.append(Move(position, Coordinate(position.x + 1, position.y + 2)))
        if board.is_empty(Coordinate(position.x - 1, position.y + 2)) or board.is_piece(Coordinate(position.x - 1, position.y + 2), not self.isWhite):
            legal_moves.append(Move(position, Coordinate(position.x - 1, position.y + 2)))
        if board.is_empty(Coordinate(position.x + 1, position.y - 2)) or board.is_piece(Coordinate(position.x + 1, position.y - 2), not self.isWhite):
            legal_moves.append(Move(position, Coordinate(position.x + 1, position.y - 2)))
        if board.is_empty(Coordinate(position.x - 1, position.y - 2)) or board.is_piece(Coordinate(position.x - 1, position.y - 2), not self.isWhite):
            legal_moves.append(Move(position, Coordinate(position.x - 1, position.y - 2)))
        return legal_moves
    
    
class Bishop(Piece):
    def __str__(self):
        if self.isWhite: 
            return 'B'
        else:
            return 'b'

    def get_legal_moves(self, board:Board, position):
        legal_moves = []
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x+n, position.y+n))):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y+n)))
            elif (board.is_piece(Coordinate(position.x+n, position.y+n), not self.isWhite)):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y+n)))
                break
            else: 
                break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x-n, position.y+n))):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y+n)))
            elif (board.is_piece(Coordinate(position.x-n, position.y+n), not self.isWhite)):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y+n)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x+n, position.y-n))):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y-n)))
            elif (board.is_piece(Coordinate(position.x+n, position.y-n), not self.isWhite)):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y-n)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x-n, position.y-n))):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y-n)))
            elif (board.is_piece(Coordinate(position.x-n, position.y-n), not self.isWhite)):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y-n)))
                break
            else: break
        return legal_moves
    
    
class Queen(Piece):
    def __str__(self):
        if self.isWhite: 
            return 'Q'
        else:
            return 'q'
        
    def get_legal_moves(self, board, position):
        legal_moves = []

        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x+n, position.y+n))):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y+n)))
            elif (board.is_piece(Coordinate(position.x+n, position.y+n), not self.isWhite)):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y+n)))
                break
            else: 
                break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x-n, position.y+n))):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y+n)))
            elif (board.is_piece(Coordinate(position.x-n, position.y+n), not self.isWhite)):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y+n)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x+n, position.y-n))):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y-n)))
            elif (board.is_piece(Coordinate(position.x+n, position.y-n), not self.isWhite)):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y-n)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x-n, position.y-n))):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y-n)))
            elif (board.is_piece(Coordinate(position.x-n, position.y-n), not self.isWhite)):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y-n)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x+n, position.y))):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y)))
            elif (board.is_piece(Coordinate(position.x+n, position.y), not self.isWhite)):
                legal_moves.append(Move(position, Coordinate(position.x+n, position.y)))
                break
            else: 
                break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x-n, position.y))):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y)))
            elif (board.is_piece(Coordinate(position.x-n, position.y), not self.isWhite)):
                legal_moves.append(Move(position, Coordinate(position.x-n, position.y)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x, position.y+n))):
                legal_moves.append(Move(position,Coordinate(position.x, position.y+n)))
            elif (board.is_piece(Coordinate(position.x, position.y+n), not self.isWhite)):
                legal_moves.append(Move(position,Coordinate(position.x, position.y+n)))
                break
            else: break
        for n in range(1, 8):
            if (board.is_empty(Coordinate(position.x, position.y-n))):
                legal_moves.append(Move(position,Coordinate(position.x, position.y-n)))
            elif (board.is_piece(Coordinate(position.x, position.y-n), not self.isWhite)):
                legal_moves.append(Move(position,Coordinate(position.x, position.y-n)))
                break
            else: break
        return legal_moves 
    
    
class King(Piece):
    def __str__(self):
        if self.isWhite: 
            return 'K'
        else:
            return 'k'
        
    def __init__(self, isWhite):
        hasMoved = False
        super().__init__(isWhite)

    def get_legal_moves(self, board, position):
        legal_moves = []
        return legal_moves


class Game:
    def __init__(self):
        self.board = Board
        self.white_turn = 1




board = Board()
all_moves = board.get_all_legal_moves(1)
for moves in all_moves:
    print(str(moves))

    



    
""":
    class Game:
        pieceCheck = {}
        def __str__(self):
            result = "    0 1 2 3 4 5 6 7\n   ----------------\n"
            for y in range(8):
                result += str(y) + ' |'
                for x in range(8):
                    result += " " + self.board[y][x]
                result += "\n"
            return result
                     
            

        def checkOutofBounce(self, pos):
            return pos.x in range(8) and pos.y in range(8)            
    

        def checkBlackPawnMove(self, pos, dest):
            if self.board[dest.y][dest.x] == '*' and dest.x == pos.x and dest.y == pos.y-1:
                return True
            elif self.board[pos.y-1][pos.x] == '*' and self.board[pos.y-2][pos.x] == '*' and dest.x == pos.x and (pos.y == 6 and dest.y == 4):
                return True
            elif dest.x == pos.x+1 and dest.y == pos.y-1 and self.board[pos.y-1][pos.x+1] != '*':
                return True
            elif dest.x == pos.x-1 and dest.y == pos.y-1 and self.board[pos.y-1][pos.x-1] != '*':
                return True
            else:
                return False


        def checkWhitePawnMove(self, pos, dest):
            if self.board[dest.y][dest.x] == '*' and dest.x == pos.x and dest.y == pos.y+1:
                return True
            elif self.board[pos.y+1][pos.x] == '*' and self.board[pos.y+2][pos.x] == '*' and dest.x == pos.x and (pos.y == 1 and dest.y == 3):
                return True
            elif self.board[pos.y+1][pos.x+1] != '*' and dest.x == pos.x+1 and dest.y == pos.y+1:
                return True
            elif self.board[pos.y+1][pos.x-1] != '*' and dest.x == pos.x-1 and dest.y == pos.y+1:
                return True
            else:
                return False

        def checkPawnMove(self, pos, dest):
            if self.board[pos.y][pos.x] == 'P':
                return self.checkWhitePawnMove(pos,dest)
            else:
                return self.checkBlackPawnMove(pos,dest)

             

        def checkRookMove(self, pos, dest):
            if not pos.x == dest.x and not pos.y == dest.y:
                  print("not straight")
                  return False
            for x in range(pos.x+1, dest.x):
                 if self.board[pos.y][x] != '*':
                    print("cant jump")
                    return False
            for y in range(pos.y+1, dest.y):
                 if self.board[y][pos.x] != '*':
                    print("cant jump")
                    return False
            for y in range(pos.y-1, dest.y, -1):
                 if self.board[y][pos.x] != '*':
                    print("cant jump")
                    return False
            for y in range(pos.y-1, dest.y, -1):
                 if self.board[y][pos.x] != '*':
                    print("cant jump")
                    return False
            return True


        def checkBishopMove(self, pos, dest):
            xdif = dest.x - pos.x  
            ydif = dest.y - pos.y
            if abs(xdif) != abs(ydif):
                print("not horizontal")
                return False
            xpar = xdif // abs(xdif)
            ypar = ydif // abs(ydif)
            for n in range(1,abs(xdif)):
                if self.board[pos.y+n*ypar][pos.x+n*xpar] != '*':
                    print(f"cant jump: {xpar} {ypar}")
                    return False
            return True
        
        def checkKnightMove(self, pos, dest):
            xdif = dest.x - pos.x  
            ydif = dest.y - pos.y
            if (abs(xdif) == 1 and abs(ydif) == 2) or (abs(xdif) == 2 and abs(ydif) == 1):
                return True
            return False
        

        def checkQueenMove(self, pos, dest):
            if self.checkRookMove(pos, dest) or self.checkBishopMove(pos, dest):
                return True
            else: 
                return False
        

        def checkKingMove(self, pos, dest):
            if abs(pos.x - dest.x) > 1 or abs(pos.y - dest.y) > 1:
                return False
            # simulate position
            temp = self.board[dest.y][dest.x]
            self.board[dest.y][dest.x] = self.board[pos.y][pos.x]
            if self.ischecked(dest):
                #end simulation
                self.board[dest.y][dest.x] = temp
                return False
            # end simulation
            self.board[dest.y][dest.x] = temp
            return True
        



        def ischecked(self, pos):
            for y in range(8):
                for x in range(8):
                    if (self.board[y][x].islower() and self.board[pos.y][pos.x].isupper()) or (self.board[y][x].isupper() and self.board[pos.y][pos.x].islower()):
                        if self.checkMove(Coordinate(x,y), pos):
                            return True
            return False
        

        def checkMove(self, pos, dest):
            if pos == dest:
                print("you have to move")
                return False
            if not self.checkOutofBounce(pos) or not self.checkOutofBounce(dest):
                print("outOfBounce")
                return False
            if self.board[pos.y][pos.x] == '*':
                print("Not a piece!")
                return False
            if (self.board[dest.y][dest.x].isupper() and self.board[pos.y][pos.x].isupper()) or (self.board[dest.y][dest.x].islower() and self.board[pos.y][pos.x].islower()):
                print(f"{str(self.board[pos.y][pos.x])} Can't take your own piece")
                return False
            if not self.pieceCheck[self.board[pos.y][pos.x]](pos, dest):
                print("illegal Move")
                return False  
            return True
        


        def move(self, pos, dest):
            # check if is checked
            for y in range(8):
                for x in range(8):
                    if (self.board[y][x] == 'K' and self.board[pos.y][pos.x].isupper()) or (self.board[y][x] == 'k' and self.board[pos.y][pos.x].islower):
                        if self.ischecked(Coordinate(x,y)) and (self.board[pos.y][pos.x] != 'K' and self.board[pos.y][pos.x] != 'k'):
                            return False
            # check move
            if not self.checkMove(pos, dest):
                return False
            # move
            self.board[dest.y][dest.x] = self.board[pos.y][pos.x]
            self.board[pos.y][pos.x] = '*'
            # turn pawn into queen
            if self.board[dest.y][dest.x] == 'P' and dest.y == 7:
                self.board[dest.y][dest.x] = 'Q'
            if self.board[dest.y][dest.x] == 'p' and dest.y == 0:
                self.board[dest.y][dest.x] = 'q'
            return True     
        


        def __init__(self):
            self.board = [
        ['R','H','B','K','Q','B','H','R'],
        ['P','P','P','P','P','P','P','P'],
        ['*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*'],
        ['p','p','p','p','p','p','p','p'],
        ['r','h','b','k','q','b','h','r']
        ]
            self.pieceCheck = {'P':self.checkPawnMove, 'R':self.checkRookMove, 'B':self.checkBishopMove, 'H': self.checkKnightMove, 'Q' : self.checkQueenMove, 'K' : self.checkKingMove,
                               'p':self.checkPawnMove, 'r':self.checkRookMove, 'b':self.checkBishopMove, 'h': self.checkKnightMove, 'q' : self.checkQueenMove, 'k' : self.checkKingMove}



    board = Board()


    print(board)

"""