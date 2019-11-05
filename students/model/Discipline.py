class Discipline:
    def __init__(self, id, name):
        '''
        in:id, name
        pre: id - integer
             name - string  
        '''
        
        self.__id = id
        self.__name = name
        
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def __str__(self):
        return str(Discipline.get_id(self)) +", " + Discipline.get_name(self)
     
    def __eq__(self,other):
        if type(other) == int:
            return self.get_id() == other 
        return self.get_id() == other.get_id()