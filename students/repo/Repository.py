from errors.Errors import RepoError 

class Repository(object):
    
    
    def __init__(self):
        self._elems = []
    
    def __len__(self):
        return len(self._elems)   
    
    def add(self, elem):
        '''
        Function that adds an element to the list 
        in: elem
        out: list U elem
        raise RepoError if the elem already exists
        '''
        
        if elem in self._elems:
            raise RepoError("Existing element!\n")
        self._elems.append(elem)
    
    def getAll(self):
        return self._elems[:]
    
    def search(self, elem):
        '''
        Function that search an element in list
        in: elem
        out:elem'
        post elem' is the element with elem id 
        raise RepoError if the elem doesn't exist
        '''
        
        if elem not in self._elems:
            raise RepoError("Inexisting element!\n")
        for x in self._elems:
            if x == elem:
                return x
    
    def update(self,elem):
        '''
        Function that updates an element
        raise RepoError if the elem doesn't exist
        '''
        if elem not in self._elems:
            raise RepoError("Inexisting element!\n")
        for i in range(len(self._elems)):
            if self._elems[i]==elem:
                self._elems[i]=elem
                return
    
    def remove(self, elem):
        '''
        Function that removes an element from the list 
        in: elem
        out: list\ elem
        raise RepoError if the elem doesn't exist
        '''
        if elem not in self._elems:
            raise RepoError("Inexisting element!\n")
        for i in range(len(self._elems)):
            if self._elems[i]==elem:
                del self._elems[i]
                return


class Undo_Repository(object):
    
    
    def __init__(self):
        self.__operations = []
        self.__index = 0
        
    def set_index(self, value):
        self.__index = value 
    
    def get_index(self):
        return self.__index
    
    def getAll(self):
        return self.__operations
    
    
    def add(self, operation, position):
        if position < len(self.__operations):
            self.__operations.insert(position,operation) 
        else: 
            self.__operations.append(operation)
