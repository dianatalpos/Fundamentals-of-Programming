from errors.Error import RepoError
from model.Ski_jump import Ski_jump

class Repository():
    def __init__(self):
        self._skiJumps = []
    
    def getAll(self):
        return self._skiJumps
    
    def add(self, elem):
        self._skiJumps.append(elem)
        
class RepositoryFile(object):
    
    def __init__(self, filename):
        Repository.__init__(self)
        self.__filename = filename
        self.__readAllFromFile()
    
    def __readAllFromFile(self):
        try:
            with open(self.__filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    line= line.strip()
                    if line != "":
                        words = line.strip().split(",")
                        name = words[0]
                        time = float(words[1])
                        average_speed = int(words[2])
                        wind = int(words[3])
                        ski_jump = Ski_jump(name, time, average_speed, wind)
                        self._skiJumps.append(ski_jump)
        except FileNotFoundError as fe:
            print("Inexisting file!")
    
    def getAll(self):
        '''
        Returns all the elements of the list
        '''
        
        return self._skiJumps

