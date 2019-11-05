from domain.Entities import Board
from errors.Errors import GameException
from random import choice

class Nega:
    
    def __init__(self,board):
        self.board = board
    
    
           
    def negamex(self,board, color):
        if self.get_nb() == 42:
            return 0

            
        columns = self._board.get_columns_not_full()
        
        for column in columns:
            copy = self._board.copy()
            copy.move(column+1, 'yellow')
            
            if copy.is_won() == True:
                
                return 43- self.get_nb()
                
        bestscore = -42
        for i in range(0,7):
            if self.can_play(i):
                copy = self._board.copy()
                copy.move(column+1, color)
                if color == 'red':
                    copy.negamax('yellow')
                else:
                    copy.negamex('red')
                
                    
   



class Game(object):
    
    def __init__(self):
        self._board = Board()
        
    def get_board(self):
        return self._board
    
    def move_human(self, column):
        self._board.move(column, 'red')
            

    def negamax(self,board, color):
        
        #print(board, color, board.get_nb())
        #return
        if board.get_nb() == 4:
            return [0,-1]
        print(board.get_nb())
        

            
        columns = board.get_columns_not_full()
        
        for column in columns:
            copy = board.copy()
            copy.move(column+1, color)
            
            if copy.is_won() == True:
                return [43- board.get_nb(), column]
                
        bestscore = -42
        pos = -1
        for i in range(0,7):
            
            if board.can_play(i):
                
                #print("board initial", board)
                copy = board.copy()
                #print("board copy", copy)
                
                copy.move(i+1, color)
                
                #print("move ", i, color)
                
                #print("copy cu move", copy)
                #return
                
                if color == 'red' :
                    score = self.negamax(copy,'yellow')[0]
                else:
                    score = self.negamax(copy,'red')[0]
                if (score>bestscore):
                    bestscore = score
                    pos = i 
        return [bestscore, pos]
    
    
    def move_computer(self):
        
        columns = self._board.get_columns_not_full()

        
        if len(columns) == 0:
            raise GameException("Board is full!")
        
        for column in columns:
            copy = self._board.copy()
            copy.move(column+1, 'yellow')
            
            if copy.is_won() == True:
                self._board.move(column+1, 'yellow')
                return
            
        for column in columns:
            
            copy = self._board.copy()
            
            copy.move(column+1,'red')
            
            if copy.is_won() == True:
                self._board.move(column+1, 'yellow')
                return
    
        
        self._board.move(choice(columns)+1, 'yellow')
        

        '''res = self.negamax(self._board, 'yellow')
        if (res[1] == -1):
            return 
        self._board.move(res[1]+1, 'yellow')
        '''