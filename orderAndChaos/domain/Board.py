from errors.Errors import GameError
from texttable.texttable import Texttable 
import copy
from domain.Square import Square


class Board(object):
    
    
    def __init__(self):
        self.__board = [[0]*6 , [0]*6, [0]*6, [0]*6, [0]*6, [0]*6]
        self.__nr_x = 0
        self.__nr_o = 0
        
    def get_x(self):
        return self.__nr_x
    
    def get_o(self):
        return self.__nr_o
    
    
    def __str__(self):
        t = Texttable()
        symbol = { 0 : " ", 1: "x", 2: 'o' }
        for i in range(0,6):
            lst = self.__board[i][:]
            for j in range(0,6):
                lst[j] = symbol[lst[j]]
            
            t.add_row(lst)
        
        return t.draw()
    
    def copy(self):
        '''
        Function that returns a copy of the board
        '''
        b = Board()
        b.__board = copy.deepcopy(self.__board)
        return b
      
    def _make_move(self, square, nb):
        self.__board[square.get_row()-1][square.get_column()-1] = nb
        
               
    def move(self, square, symbol):
        if symbol != "x" and symbol != "o":
            raise GameError("The symbol must be x or o !!")
        if (square.get_row()>6 or square.get_row()<1) and (square.get_column()<1 or square.get_row()>6):
            raise GameError("Illegal move! You need to make a move on the board!")
        if self.__board[square.get_row()-1][square.get_column()-1] != 0:
            raise GameError("This square is already filled!")
         
        if symbol == "x":
            self._make_move(square, 1)
            self.__nr_x +=1
        else:
            self._make_move(square, 2)
            self.__nr_o +=1
    
    def get_empty_squares(self):
        list = []
        for i in range(0,6):
            for j in range(0,6):
                if self.__board[i][j] == 0:
                    square = Square(i+1,j+1)
                    list.append(square)
                    
        return list
    
    def is_order(self):
        pass          
    
    def is_chaos(self):
        list = self.get_empty_squares()
        if len(list) == 0:
            return True
        else:
            return False
        
    def is_order(self):
        '''
        verify on the lines and columns
        '''
        for i in range(0,6):
            for j in range(0,2):
                if self.__board[i][j] == self.__board[i][j+1] == self.__board[i][j+2] == self.__board[i][j+3] ==self.__board[i][j+4] == 1 or self.__board[j][i] == self.__board[j+1][i] == self.__board[j+2][i] == self.__board[j+3][i] == self.__board[j+4][i] == 1:
                    return True  
                 if self.__board[i][j] == self.__board[i][j+1] == self.__board[i][j+2] == self.__board[i][j+3] ==self.__board[i][j+4] == 2 or self.__board[j][i] == self.__board[j+1][i] == self.__board[j+2][i] == self.__board[j+3][i] == self.__board[j+4][i] == 2:
                    return True  
        '''
        verify on the diagonals
        '''
        for i in range(0,2):
            for j in range(0,2):
                if self.__board[i][j] == self.__board[i+1][j+1] == self.__board[i+2][j+2] ==self.__board[i+3][j+3] ==self.__board[i+4][j+4] ==1 :
                    return True  
                if  self.__board[i][5-j] == self.__board[i+1][5-j-1] == self.__board[i+2][5-j-2] ==self.__board[i+3][5-j-3] ==self.__board[i+4][5-j-4] ==1:
                    return True
                if self.__board[i][j] == self.__board[i+1][j+1] == self.__board[i+2][j+2] ==self.__board[i+3][j+3] ==self.__board[i+4][j+4] ==2 :
                    return True  
                if  self.__board[i][5-j] == self.__board[i+1][5-j-1] == self.__board[i+2][5-j-2] ==self.__board[i+3][5-j-3] ==self.__board[i+4][5-j-4] ==2:
                    return True
        return False
    

