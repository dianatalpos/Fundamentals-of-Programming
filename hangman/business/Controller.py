from random import choice


class Service(object):
    
    
    def __init__(self, repo_sentences, validator):
        self.__repo = repo_sentences
        self.__valid = validator
        
        
    def add_sentence(self,sentence):
        
        self.__valid.valid_sentence(sentence)
        self.__repo.add()
    
    def get_hangman(self):
        number = self.__repo.get_hangman()
        hangman = ''
        word = "hangman"
        i = 0
        while i< number:
            hangman += word[i]
            i+=1
        return hangman
    
    def check_letter(self, letter):
        sentence = self.__repo.get_sentence()
        if letter not in sentence or letter in self.__repo.get_code():
            self.__repo.set_hangman(self.__repo.get_hangman()+1)
        else:
            i = 0
            for l in sentence:
                if l == letter:
                    code = self.__repo.get_code()
                    code = code[:i] + l + code[i+1:]
                    self.__repo.set_code(code)
                i+=1    
            
        
    
    def get_code(self):
        return self.__repo.get_code()
     
    def start_game(self):
        self.__repo.get_random_sentence()
        
    def is_lose(self):
        if self.__repo.get_hangman == 7:
            return True
        return False
    
    def is_win(self):
        if self.__repo.get_sentence() == self.__repo.get_code():
            return True
        return False
    



