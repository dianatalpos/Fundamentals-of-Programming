from errors.Errors import ValidError, RepoError

class Console(object):
    
    
    def __init__(self, serv):
        self.__serv = serv
        
    
    def menu(self):
        print("The commands are:")
        print("\tAdd a new sentence (add)")
        print("\tPlay hangman (play)")
        print("\tExit (exit)")
    
    
    def __ui_add(self, sentence):
        if len(sentence) =="":
            print("This sentence doesn't have words!")
            return
        
        self.serv.add_sentence(sentence) 
    
    def print_sentence(self,sentence):
        output = "\""
        for l in sentence:
            if l == '_':
                output += " _"
            else:
                output += l 
        output += "\" - \""
        output += self.__serv.get_hangman()
        output +="\""
        print(output)
        
    
    def __ui_play(self):
        self.__serv.start_game()
        self.print_sentence(self.__serv.get_code())
        while self.__serv.is_win() == False and self.__serv.is_lose() == False:
            x = input("Give a letter: ")
            x = x.strip()
            if len(x) == 1:
                try:
                    self.__serv.check_letter(x)
                    self.print_sentence(self.__serv.get_code())
                except RepoError as re:
                    print(re)
            else:
                print("You need to give a single letter!")
        if self.__serv.is_win() == True:
            print("Congrats! You won!")
        if self.__serv.is_lose() == True:
            print("You lost! Try again!")
            
    def run(self):
        while True:
            self.menu()
            x = input("Give a command: ")
            x = x.strip()
            if x == "add":
                x = input("Give sentence: ")
                x = x.strip()
                try:
                    self.__ui_add(x)
                except ValidError as ve:
                    print(ve)
                except RepoError as re:
                    print(re)
            elif x == "play":
                self.__ui_play()
            elif x== "exit":
                return
            else:
                print("Invalid command!")
        
        
        