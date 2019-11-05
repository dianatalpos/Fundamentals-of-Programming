from errors.Errors import RepoError
from random import choice

class Repository(object):
    
    
    def __init__(self):
        self._sentences = []
        self.__filename = "C:\\Andrea\\eclipse-python\\hangman\\sentences"
        self.__readAllFromFile()
        self.__sentence = ''
        self.__code = ''
        self.__hangman = 0
        self.letters = "" 
    
    def search(self, line):
        for sentence in self.__sentences:
            if sentence == line:
                return True
        return False
        
    def add(self, sentence):
        if self.search(sentence) == False:
            self._sentences.append(sentence)
            self.__writeAllToFile()
            return
        raise RepoError("Existent sentence!!")
    
    def __readAllFromFile(self):
        
        try:
            with open(self.__filename, "r" ) as f:
                lines = f.readlines()
                for line in lines:
                    sentence = line.strip()
                    self._sentences.append(sentence)  
                
        except FileNotFoundError as fe:
            print("Inexistent file!")
      
    def __writeAllToFile(self):
        try:
            with open(self.__Sfilename, "w") as f:
                for sentence in self._sentences:
                    f.write(sentence)
            
        except FileNotFoundError as fe:
            print("Inexistent file!")  
    
    def getAll(self):
        return self.__sentences
    

    def get_sentence(self):
        return self.__sentence


    def get_code(self):
        return self.__code
    
    def set_code(self, code):
        self.__code = code[:]


    def get_hangman(self):
        return self.__hangman
    
    def set_hangman(self, value):
        self.__hangman = value

    
    def code_sentence(self,sentence):
        new = ''
        words = sentence.split(" ")
        letters = ''
        
        for i in range(len(words)):
            letters += words[i][0] + words[i][len(words[i])-1]
        
        self.__letters = letters
        
        for i in range(len(words)):
            for j in range(0,len(words[i])):
                if words[i][j] in letters:
                   new +=words[i][j]
                else:
                    new += '_'
            new += ' '
        return new.strip()
    
    def get_random_sentence(self):
        print(self._sentences)
        self.__sentence = ""
        self.__code = ""
        self.__letters = ""
        self.__sentence = choice(self._sentences)
        self.__code = self.code_sentence(self.__sentence)
        self.__hangman = 0
    
    

    sentence = property(get_sentence, None, None, None)
    code = property(get_code, None, None, None)
    hangman = property(get_hangman, None, None, None)
        
    

