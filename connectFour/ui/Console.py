from errors.Errors import GameException
class Console(object):
    
    
    def __init__(self, game):
        self._game = game
    
    def read_move(self):
        while True:
            try:
                column = input("Enter column>").split(" ")
                return int(column[0])
            except Exception as e:
                print(e)
       
    
    def start(self):
        player_move = True
        print("Your color is red!")
        
        while self._game.get_board().is_won() == False and self._game.get_board().is_equality() == False:
            if player_move == True:
                print(self._game.get_board())
                col = self.read_move()
                try:
                    self._game.move_human(col)
                except GameException as ge:
                    print(ge)
            else:
                self._game.move_computer()
            player_move = not player_move
            
        print("Game over!")
        print(self._game.get_board())
        if self._game.get_board().is_won():
            if player_move == True:
                print("Computer wins!")
            else:
                print("Player wins!")
        else:
            print("It's a tie!")
        
        


