class StudentAvgDTO(object):

    
    def __init__(self, id, name, avg):
        self.__id = id
        self.__name = name
        self.__avg = avg

    def get_id(self):
        return self.__id


    def get_name(self):
        return self.__name


    def get_avg(self):
        return self.__avg 
    
    def __str__(self):
        return "(Id: " + str(self.__id)+ ") " + self.__name + " has an average of " + str(self.__avg)
    
    def __eq__(self, other):
        return self.get_avg() == other.get_avg()
    
    name = property(get_name, None, None, None)
    avg = property(get_avg, None, None, None)
    id = property(get_id, None, None, None)
    
    
    


class StudentFailDTO(object):
    
    
    def __init__(self, id, name, no_discipline):
        self.__id = id
        self.__name = name
        self.__no_discipline = no_discipline

    def get_id(self):
        return self.__id


    def get_name(self):
        return self.__name


    def get_no_discipline(self):
        return self.__no_discipline
    
    def __str__(self):
        return "(Id : " + str(self.__id) + ") " + str(self.__name) + " is failing at: " + str(self.__no_discipline)+ " disciplines."

    def __lt__(self, other):
        return self.get_no_discipline() < other.get_no_discipline() 
   
    id = property(get_id, None, None, None)
    name = property(get_name, None, None, None)
    no_discipline = property(get_no_discipline, None, None, None)
