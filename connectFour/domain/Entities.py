import copy
from errors.Errors import GameException
from texttable.texttable import Texttable

class Board(object):
    def __init__(self):
        
        self.__data = [ [0] * 7, [0] * 7, [0] * 7, [0] * 7, [0] * 7, [0] *7 ]
        self._nb = 0

    def copy(self):
        '''
        Function that returns a copy of the board
        '''
        b = Board()
        b.__data = copy.deepcopy(self.__data)
        b._nb = self._nb
        return b
    
    def get_columns_not_full(self):
        res = []
        for i in range(0,7):
            if self.__data[5][i] == 0:
                res.append(i)
        return res
    
    def can_play(self, column):
        return self.__data[5][column] == 0
    
    def get_nb(self):
        return self._nb 
    
    def is_won(self):
        for i in range(0,3):
            for j in range(0,4):
                # verify the line
                if self.__data[i][j] == self.__data[i][j+1] == self.__data[i][j+2] == self.__data[i][j+3] == 1 or self.__data[i][j] == self.__data[i][j+1] == self.__data[i][j+2] == self.__data[i][j+3] == 2:
                    return True
                #verify the column
                if self.__data[i][j] == self.__data[i+1][j] == self.__data[i+2][j] == self.__data[i+3][j] == 1 or  self.__data[i][j] == self.__data[i+1][j] == self.__data[i+2][j] == self.__data[i+3][j] == 2:
                    return True
                #verify the diagonal
                if self.__data[i][j] == self.__data[i+1][j+1] == self.__data[i+2][j+2] == self.__data[i+3][j+3] == 1 or self.__data[i][j] == self.__data[i+1][j+1] == self.__data[i+2][j+2] == self.__data[i+3][j+3] == 2:
                    return True
        
        for j in [4,5,6]:
            for i in[0,1,2]:
                if self.__data[i][j] == self.__data[i+1][j] == self.__data[i+2][j] == self.__data[i+3][j] == 1 or  self.__data[i][j] == self.__data[i+1][j] == self.__data[i+2][j] == self.__data[i+3][j] == 2:
                    return True
        for i in[3,4,5]:
            for j in [0,1,2,3]:        
                if self.__data[i][j] == self.__data[i][j+1] == self.__data[i][j+2] == self.__data[i][j+3] == 1 or self.__data[i][j] == self.__data[i][j+1] == self.__data[i][j+2] == self.__data[i][j+3] == 2:
                    return True
        for j in range(6, 2, -1):
            for i in range(0,3):
                if self.__data[i][j] == self.__data[i+1][j-1] == self.__data[i+2][j-2] == self.__data[i+3][j-3] == 1 or self.__data[i][j] == self.__data[i+1][j-1] == self.__data[i+2][j-2] == self.__data[i+3][j-3] == 2:
                    return True
                
        
        return False
    
    def is_equality(self):
        return self.is_won() == False and len(self.get_columns_not_full()) == 0
    
    def __make_move(self, column, number):
        for i in range(0,6):
            if self.__data[i][column] == 0:
                self.__data[i][column] = number
                self._nb = self._nb + 1 
                return
        
    
    def move(self, column, color):
        if color not in ['red', 'yellow']:
            raise GameException("Invalid color!")
        if column not in [1,2,3,4,5,6,7]:
            raise GameException("Move outside the board!")
        columns = self.get_columns_not_full()
        if column-1 not in columns:
            raise GameException("This column is full!")
        
        dic = {"red":1, 'yellow':2}
        self.__make_move(column-1, dic[color])
       
    def __str__(self):
        
        t = Texttable()
        d = {0 :" ", 1:"red", 2:"yellow"}
        
        for i in range(5, -1, -1):
            lst = self.__data[i][:]
            for j in [0, 1, 2, 3, 4, 5, 6]:
                lst[j] = d[lst[j]]
            t.add_row(lst)
        return t.draw()

            
                