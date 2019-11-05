from texttable import Texttable
from random import choice
import copy

class GameException(Exception):
    def __init__(self, m):
        self._msg = m
        
    @property
    def message(self):
        return self._msg

class Square():
    '''
    Represents one square of the game board
    '''
    def __init__(self, row, col):
        self._row = row
        self._col = col
        
    @property
    def row(self):
        return self._row
    
    @property
    def col(self):
        return self._col

'''
    0 - empty square
    1 - X
    2 - O 
'''
class Board():
    def __init__(self):
        '''
        Representation of the board
        '''
        self._data = [ [0] * 3, [0] * 3, [0] * 3]

    def copy(self):
        '''
        Copy the board to make sure we don't alter it while 'thinking ahead'
        '''
        b = Board()
        b._data = copy.deepcopy(self._data)
        return b

    def getEmptySquares(self):
        res = []
        for i in range(3):
            for j in range(3):
                if self._data[i][j] == 0:
                    res.append(Square(i, j))
        return res    

    def isWon(self):
        d = self._data
        
        #lines & columns
        for i in [0,1,2]:
            if d[i][0] * d[i][1] * d[i][2] in [1,8]:
                return True
            if d[0][i] * d[1][i] * d[2][i] in [1,8]:
                return True
        # diagonals
        if d[0][0] * d[1][1] * d[2][2] in [1,8]:
            return True
        if d[2][0] * d[1][1] * d[0][2] in [1,8]:
            return True        
        
        return False
    
    def isTie(self):
        return self.isWon() == False and len(self.getEmptySquares()) == 0

    '''
    square -  Square instance
    symbol - One of X or O
    '''
    def move(self, square, symbol):
        if square.row not in [0, 1, 2] or square.col not in [0, 1, 2]:
            raise GameException("Move outside board!")
        if symbol not in ['X', 'O']:
            raise GameException("Invalid symbol!")
        d = self._data
        if d[square.row][square.col] != 0:
            raise GameException("Square already taken!")
        
        ds = {'X':1, 'O':2}
        d[square.row][square.col] = ds[symbol] 

    def __str__(self):
        t = Texttable()
        d = {0 :" ", 1:"X", 2:"O"}
        
        for i in [0, 1, 2]:
            lst = self._data[i][:]
            for j in [0, 1, 2]:
                lst[j] = d[lst[j]]
            t.add_row(lst)
        return t.draw()

class Game:
    def __init__(self):
        self._board = Board()
        
    @property
    def board(self):
        return self._board

    def moveHuman(self, square):
        self.board.move(square, 'X')
    
    def moveComputer(self):
        options = self.board.getEmptySquares()
        if len(options) == 0:
            raise GameException("Board is full!")
        
        '''
        Try to win !!!
        '''
        for option in options:
            '''
            1. create board copy
            2. try move
            3. check for win
            '''
            b = self.board.copy()
            b.move(option,'O')
            
            if b.isWon() == True:
                self.board.move(option, 'O')
                return
        
        '''
        Prevent human win!
        '''
        for option in options:
            '''
            1. create board copy
            2. try move
            3. check for win
            '''
            b = self.board.copy()
            b.move(option,'X')
            
            if b.isWon() == True:
                self.board.move(option, 'O')
                return        
        
        
        self.board.move(choice(options), 'O')


class UI:
    def __init__(self, g):
        self._game = g
        
    def _readMove(self):
        while True:
            try:
                tokens = input("Enter move>").split(" ")
                return Square(int(tokens[0]), int(tokens[1]))
            except Exception as e:
                print("Invalid move!")
       
        
    def start(self):
        b = self._game.board

        playerMove = True        
        while b.isWon() == False and b.isTie() == False:
            if playerMove:
                print(b)
                move = self._readMove()
                self._game.moveHuman(move)
            else:
                self._game.moveComputer()
            playerMove = not playerMove

        print("Game over!")
        print(b)
        if b.isWon():
            if playerMove == True:
                print("Computer wins!")
            else:
                print("Player wins!")
        else:
            print("It's a tie!")

g = Game()
ui = UI(g)
ui.start()




