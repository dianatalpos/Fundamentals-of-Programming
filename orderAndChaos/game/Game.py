from domain.Board import Board
from domain.Square import Square
from random import choice 

class Game(object):
    
    
    def __init__(self):
        self.__board = Board()
    
    def get_board(self):
        return self.__board
    
    def move_human(self, row, column, symbol):
        square = Square(row, column)
        self.__board.move(square, symbol)
    
    def move_computer(self):
        
        
        '''
        Verify if the computer can win with this move
        '''
        
        empty_squares = self.__board.get_empty_squares()
        
        for square in empty_squares:
            b = self.__board.copy()
            b.move(square, 'x')
            if b.is_order() == True:
                self.__board.move(square, 'x')
                return 
            b = self.__board.copy()
            b.move(square, 'o')
            if b.is_order() == True:
                self.__board.move(square, 'o')
                return
        
        square = choice(empty_squares[:])
        
        if self.__board.get_x() >= self.__board.get_o():
            
            self.__board.move(square, 'x')
        
        else:
            self.__board.move(square, 'o')
        
        
        
        
        
        
        
        
        
        
        



