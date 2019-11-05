from errors.Errors import GameError


class Console(object):

    
    def __init__(self, game):
        self.__game = game
    
    def read_move(self):
        while True:
            x = input("Give the row, column, and the symbol(values are separeted by space): ")
            x = x.split(" ")
            try:
                if len(x) !=3:
                    raise ValueError
                row = int(x[0])
                column = int(x[1])
                symbol = x[2].strip()
                return [row,column,symbol]
            except ValueError as ve:
                print("The values for row and column must be integers! You must give 3 params!")
    
    def start(self):
       
        
        player = False
        
        while self.__game.get_board().is_chaos() == False and self.__game.get_board().is_order() == False:
            print(self.__game.get_board())
            if player == True:
                move = self.read_move()
                try:
                    self.__game.move_human(move[0],move[1], move[2])
                    
                except GameError as ge:
                    print(ge)
            else:
                self.__game.move_computer()
            
            player = not player
            
            
        if self.__game.get_board().is_chaos():
            print(self.__game.get_board())
            print("It's chaos! You won!")
        
        if self.__game.get_board().is_order():
            print(self.__game.get_board())
            print("It's order! Computer won!")
        
            
                
        

